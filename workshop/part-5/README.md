# Part 5 - Configuring the accelerometer

Okay, now that we have process acceleration data successfully, let's look at the
configuration options of the MMA8653FC device.

We want to create a new function and execute it before reading any other data:

```python
def configure_device():
	pass

check_device()
configure_device()

while True:
    x = read_x()
    y = read_y()
    z = read_z()
    print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
    print("[X:{}] [Y:{}] [Z:{}]\n".format(
        accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))
    sleep(200)

```

So we'll add the `configure_device()` code to configure the MMA8653FC with the
following settings:
- Enable Fast Read mode
- Set the Output Data Rate to 800 Hz
- Enable the High Resolution mode
- Disable the Self Test
- Configure the Dynamic Range to +/- 2g

### Tips

- To write to a register we send a normal I2C write command and send 2 bytes.
  - First byte is the register to write
  - Second byte is th data to write into the register
- Is good practice to place the device in STANDBY mode while writing to
  configuration register
