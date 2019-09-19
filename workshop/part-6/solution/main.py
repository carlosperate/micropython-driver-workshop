from micropython import const
import microbit
import ustruct


MMA8653_ADDR = const(0x1D)

MMA8653_OUT_X_MSB  = const(0x01)
MMA8653_OUT_Y_MSB  = const(0x03)
MMA8653_OUT_Z_MSB  = const(0x05)

MMA8653_WHOAMI = const(0x0D)
MMA8653_WHOAMI_VALUE = const(0x5A)

MMA8653_XYZ_DATA_CFG = const(0x0E)

MMA8653_CTRL_REG1 = const(0x2A)
MMA8653_CTRL_REG2 = const(0x2B)
MMA8653_CTRL_REG3 = const(0x2C)
MMA8653_CTRL_REG4 = const(0x2D)
MMA8653_CTRL_REG5 = const(0x2E)


class MMA8653FC:
    """Basic class for the MMA8653FC accelerometer."""

    def __init__(self, i2c):
        """Checks the WHO_AM_I register and configures the device."""
        self.i2c = i2c
        who_am_i_value = self.read_reg(MMA8653_WHOAMI)
        if who_am_i_value != MMA8653_WHOAMI_VALUE:
            raise Exception(
                'Read invalid WHO_AM_I value 0x{:02X}, expected 0x{:02X}'.format(
                    read_data[0], MMA8653_WHOAMI_VALUE))
        self.configure()


    def configure(self):
        """Configures the accelerometer."""
        # First place the device into standby mode, so it can be configured (CTRL_REG1 bit0 = 0)
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x00]))

        # CTRL_REG1 Fast read mode: bit 1 = 0
        #           bit 2 unused
        #           Output Data Rate: bits 3-5 = 0b000 for 800Hz
        #           Auto Sleep rate: bits 6-7 = 0b00 default to wake at 50Hz (unused feature)
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x00]))

        # CTRL_REG2 ACTIVE mode power scheme: bits 0-1: 0b10 (high resolution mode)
        #           Auto-SLEEP enable: bit 2 = 0 (sleep disable)
        #           SLEEP mode power scheme: bits 3-4 = 0b10 (high resolution mode)
        #           bit 5 unused
        #           Software Reset: bit 6 = 0 (nothing happens with 0, it resets with 1)
        #           Self-Test Enable: bit 7 = 0  (disable)
        # Enable high precision mode. This consumes a bit more power, but still only 184 uA!
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG2, 0x12]))

        # CTRL_REG3 is the Interrupt Control register, we can leave all defaults
        # CTRL_REG4 is the Interrupt Enable register, we can leave all defaults
        # CTRL_REG5 is the Interrupt Configuration register, we can leave all defaults

        # Configure for the selected g range, 0x00 = 2G
        self.i2c.write(MMA8653_ADDR,  bytes([MMA8653_XYZ_DATA_CFG, 0x00]))

        # Activate the device (CTRL_REG1 bit0 = 1)
        ctrl_reg1_value = self.read_reg(MMA8653_CTRL_REG1)
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, ctrl_reg1_value | 0x01]))

    def read_reg(self, start_reg):
        """Read an unsigned byte from a register."""
        self.i2c.write(MMA8653_ADDR, bytes([start_reg]), repeat=True)
        return self.i2c.read(MMA8653_ADDR, 1)[0]

    def read_regs(self, start_reg, how_many_reads):
        """Read a series of registers."""
        self.i2c.write(MMA8653_ADDR, bytes([start_reg]), repeat=True)
        return self.i2c.read(MMA8653_ADDR, how_many_reads)

    def read_x(self):
        x_data = self.read_regs(MMA8653_OUT_X_MSB, 1)
        # Unpack it as a signed char
        x_data = ustruct.unpack('b', x_data)[0]
        # Scale it to 0 to +/- 2000 and set orientation
        return x_data * 16 * -1

    def read_y(self):
        y_data = self.read_regs(MMA8653_OUT_Y_MSB, 1)
        # Unpack it as a signed char
        y_data = ustruct.unpack('b', y_data)[0]
        # Scale it to 0 to +/- 2000 and set orientation
        return y_data * 16 * -1

    def read_z(self):
        z_data = self.read_regs(MMA8653_OUT_Z_MSB, 1)
        # Unpack it as a signed char
        z_data =  ustruct.unpack('b', z_data)[0]
        # Scale it to 0 to +/- 2000
        return z_data * 16


if __name__ == "__main__":
    microbit.display.show(microbit.Image.HAPPY)
    acc = MMA8653FC(microbit.i2c)
    while True:
        x = acc.read_x()
        y = acc.read_y()
        z = acc.read_z()
        print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
        print("[X:{}] [Y:{}] [Z:{}]\n".format(
                microbit.accelerometer.get_x(),
                microbit.accelerometer.get_y(),
                microbit.accelerometer.get_z()))
        microbit.sleep(200)
