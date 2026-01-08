## Autonomous Snow Plow - IMU (Gyro)
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
