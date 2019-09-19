# Part 6

We can now configure the MMA8653FC and read acceleration data, so we have all
the basics covered with functions in a Python module.

For a MicroPython driver to be easily portable classes are a good option, so
let's conver all our functions in a class that can be run with a code like
this:


```python
import microbit

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
```
