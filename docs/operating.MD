### Snow Plow General Functionality and Operability

Quick Start Guide:
##### 1. Lidar IP Configuration Must Be Completed First:
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

Lidar: 
- [Lidar Overview](lidar.MD)


##### 2. Sensor Data Must Be Publishing to ROS2 Topic:

GPS: 
- [GPS Overview](GPS.MD)

IMU: 
- [IMU Overview](IMU.MD)

Motor: 
- [Motor Overview](lidar.MD)


##### 3. Confirm All Data is Being Captured"


##### 4. Complete Any Preflight Checklists and Safety Measures:


##### 4. Start the Machine:

Notes of mostly functional commands that can be used to construct the startup logic.

```
python3 /home/jetson/Desktop/Sandbox/Snow-Plow-On-Jetson/src/IMU.py & python3 /home/jetson/Desktop/Sandbox/Snow-Plow-On-Jetson/test/test_mock_gps.py & python3 /home/jetson/Desktop/Sandbox/Snow-Plow-On-Jetson/src/main.py & ros2 run sick_scan_xd /opt/ros/humble/share/sick_scan_xd/launch/sick_generic_caller sick_scan_xd_test.launch
```
