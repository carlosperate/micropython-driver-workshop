# Part 2 - Exploring I2C with the REPL

Now that we are a bit more familiar with the micro:bit and the REPL let's
explore the I2C interface:
https://microbit-micropython.readthedocs.io/en/latest/i2c.html


First, let's check what we have available in the I2C class:

```
>>> from microbit import i2c
>>> dir(i2c)
```


## Scanning I2C devices

Let's run the scan method:
https://microbit-micropython.readthedocs.io/en/latest/i2c.html#microbit.i2c.scan

```
>>> from microbit import i2c
>>> i2c.scan()
```

- What results are you getting? And how many?
- Make a note of these addresses as we will use them soon.


## I2C addresses

When the master device initialises a transaction, the first byte sent down the
wire will contain the 7-bit address of the slave devices followed by a bit to
indicate if this is a Read (1) or Write (0) operation.

While the slave addresses are 7-bit, sometimes the documentation might refer to
the "full address" as two an 8-bit addresses, one for reading and one for
writing.

For example, a slave with 7-bit address `0x05` (`0b0000101`) could also be
referred to have addresses `0xA`/`0xB` (`0b0001010`/`0b0001011`).

For this workshop we will always refer to the 7-bit address, as that's the
format used by all the methods in the MicroPython I2C class.


### MMA8653FC I2C Address

The I2C address of the accelerometer can be found in the datasheet, in one of
the tables from section 5.8 "Serial I2C Interface".

- Does the number listed in the datasheet match one of the values returned by
`i2c.scan()`?


## Talking with the accelerometer

Okay, so let's try to read something from the accelerometer!

The first thing we need to do is find a good register to read from, perhaps one
with a constant value?

Search for a register named "WHO AM I" register in the datasheet. This is a very
common register in electronic devices, and it us normally used to store a
constant value to identify the part.

I2C read operations are a two-part process:
- First send a write operation (`i2c.write()`) with the register address
- Then send a read operation (`i2c.read()`) with the number of bytes you want
  to read
    - Most devices will let you read multiple registers continuously with a
      single read operation, but let's start with reading just a single register


```
>>> i2c.write(???)
>>> result = i2c.read(???)
```

Then you can compare the data read into `result` against the value indicated in
the datasheet.

```
>>> from microbit import i2c, display, Image
>>> i2c.write(???)
>>> result = i2c.read(???)
>>> if read_data[0] == 0x5A:
>>>     display.show(Image.HAPPY)
```

### Troubleshooting

Did it work? Are you reading value `0xFF`?

This is because this device requires the read operation to be sent immediately
after the write operation without interruption (i.e. without a stop bit).

- Can you find a way in the I2C documentation to not send a stop bit before
  the read operation?
