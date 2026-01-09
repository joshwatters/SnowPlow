## Autonomous Snow Plow - IMU (Gyro)

The Snow Plow currently has multiple IMU. We use a separate BNO055 as opposed to the IMU in the Sick Scan Lidar currently. 



For IMU: [Inertial Measurement Unit](./docs/adafruit-bno055-absolute-orientation-sensor.pdf)

Currently we use the roll pitch and yaw values from the gyro read over serial.

```
// confirm usb port
lsusb
```

```
// Set baud and scan
stty -F /dev/ttyUSB0 115200
cat /dev/ttyUSB0
```
