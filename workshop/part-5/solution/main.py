from microbit import i2c, sleep, accelerometer
import ustruct


MMA8653_ADDR = 29

MMA8653_OUT_X_MSB  = 0x01
MMA8653_OUT_Y_MSB  = 0x03
MMA8653_OUT_Z_MSB  = 0x05

MMA8653_WHOAMI = 0x0D
MMA8653_WHOAMI_VALUE = 0x5A

MMA8653_CTRL_REG1 = 0x2A
MMA8653_CTRL_REG2 = 0x2B
MMA8653_CTRL_REG3 = 0x2C
MMA8653_CTRL_REG4 = 0x2D
MMA8653_CTRL_REG5 = 0x2E
MMA8653_XYZ_DATA_CFG = 0x0E


def check_device():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_WHOAMI]), repeat=True)
    read_data = i2c.read(MMA8653_ADDR, 1)
    if read_data[0] != MMA8653_WHOAMI_VALUE:
        raise Exception('Invalid WHO_AM_I value 0x{:02X}, expected 0x{:02X}'.format(read_data[0], MMA8653_WHOAMI_VALUE))


def configure_device():
    # First place the device into standby mode, so it can be configured (CTRL_REG1 bit0 = 0)
    i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x00]))

    # CTRL_REG1 Fast read mode: bit 1 = 0
    #           bit 2 unused
    #           Output Data Rate: bits 3-5 = 0b000 for 800Hz
    #           Auto Sleep rate: bits 6-7 = 0b00 default to wake at 50Hz (unused feature)
    i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x00]))

    # CTRL_REG2 ACTIVE mode power scheme: bits 0-1: 0b10 (high resolution mode)
    #           Auto-SLEEP enable: bit 2 = 0 (sleep disable)
    #           SLEEP mode power scheme: bits 3-4 = 0b10 (high resolution mode)
    #           bit 5 unused
    #           Software Reset: bit 6 = 0 (nothing happens with 0, it resets with 1)
    #           Self-Test Enable: bit 7 = 0  (disable)
    # Enable high precision mode. This consumes a bit more power, but still only 184 uA!
    i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG2, 0x12]))

    # CTRL_REG3 is the Interrupt Control register, we can leave all defaults
    # CTRL_REG4 is the Interrupt Enable register, we can leave all defaults
    # CTRL_REG5 is the Interrupt Configuration register, we can leave all defaults

    # Configure for the selected g range, 0x00 = 2G
    i2c.write(MMA8653_ADDR,  bytes([MMA8653_XYZ_DATA_CFG, 0x00]))

    # Activate the device (CTRL_REG1 bit0 = 1)
    i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1]), repeat=True)
    ctrl_reg1_value = i2c.read(MMA8653_ADDR, 1)[0]
    i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, ctrl_reg1_value | 0x01]))


def read_x():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_X_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    # Unpack it as a signed char
    result = ustruct.unpack('b', result)[0]
    # Scale it to 0 to +/- 2000 and set orientation
    return result * 16 * -1


def read_y():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_Y_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    # Unpack it as a signed char
    result = ustruct.unpack('b', result)[0]
    # Scale it to 0 to +/- 2000 and set orientation
    return result * 16 * -1


def read_z():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_OUT_Z_MSB]), repeat=True)
    result = i2c.read(MMA8653_ADDR, 1)
    # Unpack it as a signed char
    result = ustruct.unpack('b', result)[0]
    # Scale it to 0 to +/- 2000
    return result * 16


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
