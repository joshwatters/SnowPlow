## Installation:

In the event of a need for a complete reinstallation, the following process should help.

## Jetson Installation
The Jetson Nano getting started guide is located here: 

- [Getting Started with the Jetson Nano](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

Ros2 Installation:

Upon successful installation of 22.04 for Jetson, proceed to the ROS2 humble installation:

- [ROS2](https://docs.ros.org/en/humble/Installation.html) 
- Go through talker and listener to confirm ROS2 install is complete. ^^
- Install the Colcon Build Packages you want: Lidar, Slam toolbox, Nav2, turtlebot etc. Currently this project is only using the Lidar found separately below.
- [Info About Colcon Build](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)

## Lidar Installation
Vision Systems:

Sick Lidar w/ imu
- [Getting Started with the Sick 511 Video Series](https://support.sick.com/sick-knowledgebase/article/?code=KA-09385)
- [Lidar](/docs/lidar.MD)

## Pathing Options
Slam Toolbox
- [Slam](/docs/slam.MD)

Nav 2
- [Nav 2](/docs/nav2.MD)


Path Planning:
Path planning is facilitated by the previous generations git repo: 

- [SnowPlow2021](https://github.com/ISURobotics/SnowPlow2021)


Data Collection:
Data collection is facilitated by Rosbag.
Moving forward it likely makes sense to use MCAP and transition any existing Rosbags. If any data needs to be converted from ROS1:

- [Rosbag conversion ROS to ROS2](https://docs.ros.org/en/noetic/api/ov_core/html/dev-ros1-to-ros2.html)


Upon successful installation, continue to :

- [Operating Procedure](/docs/operating.MD)
