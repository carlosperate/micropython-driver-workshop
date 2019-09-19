# Part 4 - Processing the acceleration data

To understand why the values read from Part 3 are different, let's read the
MicroPython accelerometer class documentation:
https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html

> Get the acceleration measurement in the x/y/z axis, as a positive or negative
> integer, depending on the direction. The measurement is given in milli-g.
> By default the accelerometer is configured with a range of +/- 2g, and so
> this method will return within the range of +/- 2000mg.

So we should expect values between 0 and 2000, right?

- When you rotate the micro:bit (without shaking it angrily!) what kind of
maximum values do you see?

```python
from microbit import accelerometer
while True:
    print("[X:{}] [Y:{}] [Z:{}]\n".format(
        accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))
```

- Are the max values you see around 1000mg?
- How many milli-g does the earth gravitation pull generate?
    - That's right 1g or 1000mg! So the accelerometer is constantly reading the
      earth gravity as well
- Now shake the micro:bit vigorously, what maximum values do you see?
    - We should now be seeing values closer to the 2000mg theoretical maximum


Then why are we not reading those values from the accelerometer?

```python
while True:
    x = read_x()
    y = read_y()
    z = read_z()
    print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
    print("[X:{}] [Y:{}] [Z:{}]\n".format(
        accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))
```

Because the values stored in the registers represent a value within a range from
0 to 2g (as this is the default max range configured in the MMA8653FC part).

So, assuming you are only reading the MSB register (8-bits), the maximum
register value will represent 2000mg.

- What can we do to change the range from 0-255 to 0-2000?
- Does that give us the right result all the time?
    - If not, why not?
- The answer is in section 5.2 "8-bit or 10-bit data"
    - > The measured acceleration data is stored in the following registers as
      > 2’s complement...
    - Remember that the range is ±2000 mg
- The direction of some of these forces might not be correct yet?
  The fix might be simple, but can you think why it's needed?
    - Have a look at diagrams in section 5.6 "Orientation detection" and the
      placement of the accelerometer in the micro:bit board.
    - Which way is up/down or left/right?


### Tips

- The ustruct module allows you to pack and unpack in multiple data formats,
  like signed and unsigned chars (bytes)
    - https://docs.python.org/3.5/library/struct.html
    - https://docs.python.org/3.5/library/struct.html#format-characters
