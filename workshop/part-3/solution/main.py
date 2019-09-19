from microbit import i2c, sleep, accelerometer


MMA8653_ADDR = 29

MMA8653_OUT_X_MSB  = 0x01
MMA8653_OUT_Y_MSB  = 0x03
MMA8653_OUT_Z_MSB  = 0x05

MMA8653_WHOAMI = 0x0D
MMA8653_WHOAMI_VALUE = 0x5A


def check_device():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_WHOAMI]), repeat=True)
    read_data = i2c.read(MMA8653_ADDR, 1)
    if read_data[0] != MMA8653_WHOAMI_VALUE:
        raise Exception('Invalid WHO_AM_I value 0x{:02X}, expected 0x{:02X}'.format(read_data[0], MMA8653_WHOAMI_VALUE))


def read_x():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_X_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    return result[0]


def read_y():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_Y_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    return result[0]


def read_z():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_Z_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    return result[0]


check_device()

while True:
    x = read_x()
    y = read_y()
    z = read_z()
    print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
    print("[X:{}] [Y:{}] [Z:{}]\n".format(
        accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))
    sleep(100)
