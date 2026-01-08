import socket
import time
import math
from ftplib import print_line
import matplotlib.pyplot as plt
import numpy as np

telegram = "sRA LMDscandata 0 1 151FDC8 0 0 EC4B EDD5 85BF655E 85BF9621 0 0 3E 0 0 2710 21C 0 1 DIST1 3F800000 00000000 4A0E5 1A0B B5 305 30F 312 315 320 325 328 32F 0 0 B62 B35 B16 AD8 AC9 742 753 767 779 791 7A8 7B8 764 782 793 7B1 7C8 7E5 7FF 817 807 806 834 824 816 802 7F8 7E8 7DA 7C9 7B0 7AF 797 789 780 771 767 781 7AB 7A6 796 788 77F 77E 771 76B 769 751 74A 742 73A 732 731 724 71C 71C 716 70F 707 701 701 6FC 6F2 6F2 6E9 6EC 6E7 6E5 6E3 6E4 6DA 6D6 6D5 6D5 6D6 6D4 6D8 6D7 6D2 6CE 6D2 6D4 6D4 6D4 6CE 6D0 6D8 6E3 6DC 6E1 6E4 6E4 6E9 6E9 6FA 6ED 6F7 6F7 702 70A 707 712 710 71A 720 726 728 730 73C 740 74A 751 759 765 76D 770 787 78A 796 7A3 7A9 7B2 7C6 7D5 7E2 7E9 7FC 808 809 828 837 848 85B 86B 87B 88C 89B 8B3 8D1 8E8 8F8 90F 91C 93E 957 971 989 96A 94E 974 992 9B9 9CC 9E5 A11 A88 AD7 B09 B2F B59 B8A BB5 BE8 C1E C54 C85 CBD D07 D3A D81 DC6 0 0 0 0 0 0"

# --- Configuration ---
LIDAR_IP = "192.168.1.2"  # Replace with your sensor's IP address
LIDAR_PORT = 2111         # Default port for CoLa A/B communication
# The command for requesting a single scan data packet (CoLa A ASCII)
# sRN LMDscandata is the command to request the "LMDscandata" variable (the scan data) once.
REQUEST_COMMAND = b"\x02sRN LMDscandata\x03" # STX (0x02) + command + ETX (0x03)
# possible alternative:\x02sEN LMDscandata 1\x03

def request_single_packet(ip, port, command):
    """Connects to the LiDAR, sends a request, and receives one response."""
    try:
        # Create a TCP/IP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(f"Connecting to {ip}:{port}...")
            s.connect((ip, port))
            print("Connected.")

            # Send the request command
            print(f"Sending command: {command!r}")
            s.sendall(command)
            print("Command sent, waiting for response...")

            # Receive data
            # The buffer size might need adjustment depending on the scan data size
            data = s.recv(4096)
            if data:
                print("Received data:")
                # Decode the response (assuming ASCII for CoLa A)
                try:
                    decoded_data = data.decode('ascii')
                    print(decoded_data)
                    return decoded_data
                except UnicodeDecodeError:
                    print(f"Received non-ASCII data (CoLa B likely): {data!r}")
                    return data
            else:
                print("No data received.")
                return None

    except ConnectionRefusedError:
        print("Connection failed. Check IP, port, and ensure the LiDAR is powered on and connected to the network.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
def camera():
    print_line("Sick Lidar Activated")

def parse_telegram(telegram):
    tokens = telegram.split(' ')
    assert(len(tokens) > (18 + 8))
    header = tokens[:18]
    assert(header[0] == 'sRA')
    assert(header[1] == 'LMDscandata')
    sections = tokens[18:]
    assert(int(sections[0]) == 0)
    assert(int(sections[1]) == 1)
    assert(sections[2] == 'DIST1')
    assert(sections[3] in ['3F800000', '40000000'])
    scale_factor = 1 if sections[3] == '3F800000' else 2
    assert(sections[4] == '00000000')
    start_angle = int(sections[5], 16) / 10000.0
    angle_step = int(sections[6], 16) / 10000.0
    value_count = int(sections[7], 16)
    values = list(map(lambda x: int(x, 16) * scale_factor, sections[8:8+value_count]))
    angles = [start_angle + angle_step * n for n in range(value_count)]
    return (values, angles)

def to_cartesian(distances, angles):
    x = list(map(lambda r, t: r * math.cos(math.radians(t)), distances, angles))
    y = list(map(lambda r, t: r * math.sin(math.radians(t)), distances, angles))
    fig = plt.figure(figsize=(12, 7))
    ax = fig.add_subplot(111, projection='3d')
    # img = ax.scatter(xs, ys, zs, c=zs, cmap='viridis', s=0.8)
    for i in range(0, len(StoredLast[1])):
        line = plt.plot([x[i], 0],[y[i],0])
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    plt.title("Sick 511")
    plt.show()

def to_polar(distances, angles):
    angles_radians = np.radians(angles)
    lengths = distances
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    for i in range(0, len(angles)):
        ax.scatter(angles_radians, lengths, s=5, label='LiDAR Scans', color='red')
        line = plt.plot([angles_radians[i], 0], [lengths[i], 0])

    ax.scatter(0, 0, s=100, color='black', marker='+', label='LiDAR Sensor')
    ax.set_xticks(np.radians(np.arange(0, 360, 45)))
    ax.set_rmax(4500)
    ax.grid(True)
    ax.set_title("Sick 511 Polar Coordinates", va='bottom')
    plt.show()

def one_cycle(telegram):
    Parsed = (parse_telegram(telegram))
    to_cartesian(Parsed[0], Parsed[1])
    to_polar(Parsed[0], Parsed[1])
    return (Parsed)
# def log_via_websocket(array):



if __name__ == "__main__":
    # scan_data = request_single_packet(LIDAR_IP, LIDAR_PORT, REQUEST_COMMAND)
    # if scan_data:
    #     print("\nSuccessfully captured a single data packet.")
    #     StoredLast = (parse_telegram(telegram))
    #     one_cycle(telegram)

    # Snap a screenshot of the field
    StoredLast = (parse_telegram(telegram))
    one_cycle(telegram)

    # Re-evaluate Trajectory

    # Send Movement Commands