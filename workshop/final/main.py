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
        """Checks the WHO_AM_I register and initialised the device."""
        self.i2c = i2c
        who_am_i_value = self.read_reg(MMA8653_WHOAMI)
        if who_am_i_value != MMA8653_WHOAMI_VALUE:
            raise Exception(
                'Read invalid WHO_AM_I value 0x{:02X}, expected 0x{:02X}'.format(
                    read_data[0], MMA8653_WHOAMI_VALUE))
        self.initialise()


    def initialise(self):
        """Configures the accelerometer."""
        # TODO: Configure sample period

        # First place the device into standby mode, so it can be configured.
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x00]))
        # Enable high precision mode. This consumes a bit more power, but still only 184 uA!
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG2, 0x10]))
        # Enable the INT1 interrupt pin
        # self.i2c.writeRegister(MMA8653_ADDR, bytes([MMA8653_CTRL_REG4, 0x01]))
        # Select the DATA_READY event source to be routed to INT1
        # self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG5, 0x01]))
        # Configure for the selected g range, 0x00 = 2G
        self.i2c.write(MMA8653_ADDR,  bytes([MMA8653_XYZ_DATA_CFG, 0x00]))
        # Bring the device back online, with 10bit wide samples at the requested frequency.
        # TODO: Lets do 8 bits
        # value = accelerometerPeriod.get(samplePeriod * 1000);
        self.i2c.write(MMA8653_ADDR, bytes([MMA8653_CTRL_REG1, 0x01]))

    def read_reg(self, start_reg):
        """Read an unsigned byte from a register."""
        self.i2c.write(MMA8653_ADDR, bytes([start_reg]), repeat=True)
        return self.i2c.read(MMA8653_ADDR, 1)[0]

    def read_regs(self, start_reg, how_many_reads):
        """Read a series of registers."""
        self.i2c.write(MMA8653_ADDR, bytes([start_reg]), repeat=True)
        return self.i2c.read(MMA8653_ADDR, how_many_reads)

    def read_x(self):
        reg_data = self.read_regs(MMA8653_OUT_X_MSB, 1)
        return ustruct.unpack('b', reg_data)[0]

    def read_y(self):
        reg_data = self.read_regs(MMA8653_OUT_Y_MSB, 1)
        return ustruct.unpack('b', reg_data)[0]

    def read_z(self):
        reg_data = self.read_regs(MMA8653_OUT_Z_MSB, 1)
        reg_data =  ustruct.unpack('b', reg_data)[0]


if __name__ == "__main__":
    microbit.display.show(microbit.Image.HAPPY)
    acc = MMA8653FC(microbit.i2c)
    while True:
        x = acc.read_x() * 8 * 2 * -1
        y = acc.read_y() * 8 * 2 * -1
        z = acc.read_z() * 8 * 2
        print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
        print("[X:{}] [Y:{}] [Z:{}]\n".format(
                microbit.accelerometer.get_x(),
                microbit.accelerometer.get_y(),
                microbit.accelerometer.get_z()))
        microbit.sleep(200)
