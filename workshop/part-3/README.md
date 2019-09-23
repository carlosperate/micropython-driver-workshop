# Part 3 - Reading data from the accelerometer

For this exercise we will read some acceleration data from the MMA8653FC.


## Documentation You'll Need

- MMA8653FC datasheet, section 6 "Register Descriptions"


## Loading a script into the micro:bit

From this point forward we will be writing in a Python file, instead of
executing code directly in the REPL. That being said, you can still use the REPL
to try small snippets or explore the MicroPython APIs, I use it constantly when
writing code for the micro:bit!

Mu:
- Create a new file
- Add a quick script that does something with the micro:bit, for example, show
  an image on the display)
- Click the Flash button

Online Editor:
- Refresh the browser tab
- Click the Connect button
    - The Download button should now be named "Flash"
- Click the Flash button


## Create a new script

You can have a look at the solution for the previous parts if you like to
start your Python script from a known base.

We'll start simple and create a new function based on our previous REPL
experiments. We can do this to confirm we are talking with the right device:

```python
from microbit import i2c

MMA8653_ADDR = ??

MMA8653_WHOAMI = ??
MMA8653_WHOAMI_VALUE = ??


def check_device():
    i2c.write(MMA8653_ADDR, bytes([MMA8653_WHOAMI]), repeat=True)
    read_data = i2c.read(MMA8653_ADDR, 1)
    if read_data[0] == MMA8653_WHOAMI_VALUE:
        # What do we do if we find the right device?
        pass
    else:
        # What do we do if we do in this case? Maybe throw an error?
        pass

check_device()
```


## Reading acceleration data

Have a look at the datasheet Section 6.1 "Register address map", are there any
register there that could contain the X, Y, and Z acceleration?

You might also notices there is a lot of register to configure the device.
Thankfully we can count with the default values of the MMA8653FC configuration
registers to have sane values, so we can start reading data without running
an initialisation routine.

Add to your script these new functions to read the acceleration in the 3 axes:

```python
def read_x():
    pass


def read_y():
    pass


def read_z():
    pass


while True:
    x = read_x()
    y = read_y()
    z = read_z()
    print("[X:{}] [Y:{}] [Z:{}]".format(x, y, z))
```

- Does moving the micro:bit in the different axes affects the values as you
  would expect?
- What value ranges are you getting?
- Compare your results to the `microbit.accelerometer` `get_x()` `get_y()` and
  `get_z()` methods, are they the same?
    - We'll explore why not in the next part

### Tips

- `MSB` Can stand for Most Significant Bit or Most Significant Byte
- `LSB` Can stand for Least Significant Bit or Least Significant Byte
- Each axes sample is 10 bits, and as each register can only hold 1 byte there
  is one MSB and one LSB register. In these cases you can read the Most
  Significant Byte and ignore the LSB.
