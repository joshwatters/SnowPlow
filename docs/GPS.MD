# Autonomous Snowplow - GPS
## About GPS

## At a glance:

This is actual footage from our gps running on Windows. On Linux we read the data from python.

<img src="./GPSGIF.gif" width="720" height="486" />

This is sample output of longitude and latitude without RTK.

- [Sample Output Text](../src/SampleUCenterLog.txt)

Future home of example using RTK:

- [UPDATE THIS TO CORRECT FORMAT](../src/SampleUCenterLog.txt)

We will be comparing the above two methods to determine the differences in packets.

An example of reading from serial in python looks like this:

- [gps.py](../src/gps.py)
- [GPS Output](../src/gps.txt)

Snowplow's implementation is a little more complex. There are several methods of configuration for the Real Time Kinematic setup. One Zed-f9p is located on the snow plow. Real time kinematics involves an additional stationary gps base station that feeds correction data. This improves the accuracy to a point it is useable for competition. The normal method seen above recieves longitude and latitude but without thumbnail precision. In adding a second data source we are able to triangulate and further improve the accuracy. This is the reason the Raspberry PI is present currently. 

## Real Time Kinematic Data

Currently the Raspberry PI runs a python script that collects RTK data from a second source and pipes that back over usb to zed gps. The scripts are located in a gps folder in this repository. There are several options for this however the current implementation is this.
The Only Device that requires Wifi is the RPI.

Wifi should be set to:

Network: iBrick (2)

Password: password
- [Ames, Iowa](../rpi/AmesCorrectionData.sh)
- [St Paul, Minnesota](../rpi/StPaulCorrectionData.sh)

The RPI must be connected to a mobile hotspot on someones phone in order to be able to retrieve the correction data. Additionally one script needs to be run from the desktop. One is for Iowa and one is for Minnesota (competition location). Both scripts access publicly available gps data. Just connect to wifi and run the script. The bluetooth method has been tested but requires an app instead of a wifi hotspot.

## The GPS used for this project is:

- [Product Specs](https://www.sparkfun.com/sparkfun-gps-rtk-sma-kit.html)

## There are provided examples:

- [GPS Hookup Guide](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide)

- [Connect to a Correction Source](https://learn.sparkfun.com/tutorials/gps-rtk2-hookup-guide/connecting-the-zed-f9p-to-a-correction-source)

- [Setting up RTK2GO](http://rtk2go.com/how-to-connect/)

- [GPS info](http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101)

## Data Sheet:

- [Datasheet](./ZED-F9P-02B_DataSheet_UBX-21023276.pdf)


## Our implementation and scripts that reference the GPS:

- [Schematic](./SparkFun-GPS-RTK-SMA-ZED-F9P-Schematic.pdf)

- [RobotGPS.py](../src/RobotGPS.py)

- [GPS_Node.py](../src/GPS_Node.py)

