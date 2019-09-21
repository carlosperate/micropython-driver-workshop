# Part 1 - Getting to know the micro:bit

Let's start by getting familiar with the micro:bit and the REPL.


## Documentation You'll Need

- https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/images.html
- https://microbit-micropython.readthedocs.io/en/v1.0.1/accelerometer.html


## Quick Start

Connect the micro:bit to your computer using a Micro-B USB cable.
It will appear in the computer as a drive called 'MICROBIT'.

There is a hex file in this directory named `microbit-micropython-v1.0.1.hex`,
copy this file into the MICROBIT USB drive. This will flash MicroPython into
the micro:bit.

A good summary of the micro:bit features: https://microbit.org/guide/features/

![micro:bit](https://microbit.org/images/microbit-hardware-access.jpg)


## Access the REPL

If any of these steps fail, consult the [troubleshooting section from the
repository README](../../README.md#troubleshooting).

### With Mu

- Select the micro:bit mode
- Click on the REPL button

### With Online Editor

If you are using the online editor with **Chrome**:
- Go to https://python.microbit.org/v/beta
- Click the "Open Serial" button
- Select the micro:bit device


## Exploring with the REPL

In the REPL type `help()` and see what it does:

```
MicroPython v1.9.2-34-gd64154c73 on 2017-09-01; micro:bit v1.0.1 with nRF51822
Type "help()" for more information.
>>> help()
```

Make sure to read the the `help()` output, it is tremendously useful!

When you are ready, try simple commands:

```
>>> import microbit
>>> microbit.display.scroll('Hello world!')
```

Remember that you can use TAB for auto-completion, `dir()` (e.g. `dir(display)`)
and `help('modules')` to explore.

Try the following things:
- Scroll a text message on the display
- Show an Image on the display
- Show an Image on the display when button A is pressed
- Read an X, Y, or Z accelerometer values
- Show an Image on the display when the last gesture **was** `shake`
