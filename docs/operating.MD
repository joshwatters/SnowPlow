### Snow Plow General Functionality and Operability

Quick Start Guide:
## 1. Lidar IP Configuration:
Before the lidar will function, IP configuration must be complete or the Lidar will not be able to recieve packets. The current implementation 
involves using the sick_scan_xd packages that "publish" data over a ROS2 topic. (This is different from the script that is being used to generate the above images; 
It is in here to show how to parse a packet if the team decides to stray from ROS2.) This data is retrieved from the topic and used to map the snowplow to a grid. 
More or less we scan, then generate a map on an x,y and ultimately use Dijkstra's for path planning.

To ensure proper configuration, double check the following items and run the command:

```
nc -z -v -w5 192.168.1.2 2112
```


If improperly configured, it will fail with the message Network is unreachable. No progress can be made until this connects. 

If network is unreachable view and follow the steps for IP configuration. 
-Lidar: [Lidar Overview](lidar.MD)

Otherwise proceed with:

```
# Source the environment
source /opt/ros/humble/setup.bash

# Change Directory to launch folder
cd /opt/ros/humble/share/sick_scan_xd/launch

# run sick scan
ros2 run sick_scan_xd sick_generic_caller sick_lms_5xx.launch
hostname:=192.168.1.2
```


## 2. Sensor Data Publishing to ROS2 Topic:

GPS: [GPS Overview](GPS.MD), IMU: [IMU Overview](IMU.MD), Motor: [Motor Overview](lidar.MD)

Confirm data is being collected at the following locations:

IMU = '/imu/magnetometer'

GPS = '/gps_pose'

Lidar = '/cloud'

Motors = '/left_motor/speed', '/right_motor/speed'

Each data source should have a topic.

```
source /opt/ros/humble/setup.bash
ros2 topic list
```

## 4. Complete Any Preflight Checklists and Safety Measures:


## 4. Start the Machine:
Running In Operational Mode with Movement:

> [!WARNING]

> WARNING! THIS COMMAND STARTS THE MOTORS.

(Before running the main function, we need to start sick_scan_xd, Arduino_Node, and GPS_Node)
It will be something like this:

```
/home/jetson/Desktop/Sandbox/SnowPlow/src/Serial_Detect.py & python3 /home/jetson/Desktop/Sandbox/SnowPlow/src/Arduino_Node.py & python3 /home/jetson/Desktop/Sandbox/SnowPlow/src/Arduino_Node.py & ros2 run sick_scan_xd sick_generic_caller sick_scan_xd_test.launch

# Here is the previous command:

python3 src/IMU_Node.py & python3 test/test_mock_gps.py & ros2 run sick_scan_xd sick_generic_caller sick_scan_xd_test.launch

 ```
Start the robot with actual GPS, IMU and LIDAR attached and clear view of the sky:
(Use This Outside Only after familiarizing yourself with the main.py script)

This function will initialize the robot and lidar, create the object map with lidar data,
and begin motion of the robot:
```

python3 src/main.py

```
