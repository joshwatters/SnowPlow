## Autonomous Snowplow - Motors
## About Motors

Motor control is a signal sent between -100 and 100 over serial or via the controller. There is an emergency stop built into the remote controller and a physical estop on the actual SnowPlow.  The details of the wiring can be found in the wiring diagram. If the sketch is uploaded and the wires are connected to the correct place then the sensor scripts will recognize the device. The motors are wired to the motor drivers. The drivers are wired to an ardruino via jumper wires and the arduino is connected via usb to the Jetson. The serial detect script detects each usb device and maps them into the logic for the pathing. It is important that the usb and sensors be connected before powering on the Snow Plow and that the Serial_ Detect.py is run before proceeding further.

[Future Home of Motor Data Sheet](.pdf)
[Future Home of Motor Driver Data Sheet](.pdf)

```
// confirm usb port
lsusb

// Set baud and scan
stty -F /dev/ttyUSB0 115200
cat /dev/ttyUSB0

# Detect which sensor maps to each dev ie ACM0, ACM1 and use the logic pathing and main.py
source /opt/ros/humble/setup.bash
python3 /home/jetson/Desktop/Sandbox/SnowPlow/src/Serial_Detect.py 

# Each data source should have a topic. Confirm data is being collected at the following locations:
Motors = '/left_motor/speed', '/right_motor/speed'

source /opt/ros/humble/setup.bash
ros2 topic list
``````

After completing procede to: [Operating Procedure](./operating.MD)



