from microbit import i2c, display, Image

MMA8653_I2C_ADDRESS = 29

MMA8653_WHOAMI_ADDRESS = 0x0D
MMA8653_WHOAMI_VALUE = 0x5A


i2c.write(MMA8653_I2C_ADDRESS, bytes([MMA8653_WHOAMI_ADDRESS]), repeat=True)
read_data = i2c.read(MMA8653_I2C_ADDRESS, 1)
if read_data[0] == MMA8653_WHOAMI_VALUE:
    print('MMA8653 Accelerometer found at address {}'.format(MMA8653_I2C_ADDRESS))
    display.show(Image.HAPPY)
else:
    print('Invalid value 0x{:02X}, expected 0x{:02X}'.format(read_data[0], MMA8653_WHOAMI_VALUE))
    display.show(Image.SAD)
