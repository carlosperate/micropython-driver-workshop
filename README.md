# MicroPython Drivers Workshop

Welcome to the MicroPython Drivers Workshop!


## Table of Contents

- [🚀 How to use this repository](#how-to-use-this-repository)
- [📌 Requirements](#requirements)
- [📚 Documentation You Will Need](#documentation-you-will-need)
- [📑 Datasheets](#datasheets)
- [🔨 Troubleshooting](#troubleshooting)


## How To Use This Repository

If you are running the workshop in person there was an introductory presentation
explaining basic concepts and the general workflow for embedded development.

The presentation Power Point can be found at the root of this repository.
There is also a PDF version that can rendered within GitHub, so you can
[view it online](HW-Drivers-Workshop-presentation.pdf).

The `workshop` folder contains the instructions and files for the workshop.

The easiest way to follow the workshop is to read the contents directly from
GitHub, so there is no need to clone it in your computer.


## Requirements

You will need:

- A computer
- A BBC micro:bit v1.3 (v1.5 uses a different accelerometer)
- A Micro-B USB cable (the kind most phones used to have before USB-C)
    - Make sure this is not a charge-only cable
- A local micro:bit editor in your computer:
    - Mu: https://codewith.mu
    - Online Editor (Chrome preferred for WebUSB):
      https://python.microbit.org/v/beta
- Windows 7 or 8 users will need to use Mu and install this serial driver:
  https://os.mbed.com/docs/mbed-os/v5.13/tutorials/windows-serial-driver.html
- The contents of this repository
- A copy of the MMA8653FC datasheet (linked below)


## Documentation You Will Need

The micro:bit MicroPython documentation can be found here:
- https://microbit-micropython.readthedocs.io/en/v1.0.1/index.html

Specifically the micro:bit MicroPython I2C documentation:
- https://microbit-micropython.readthedocs.io/en/v1.0.1/i2c.html

MicroPython upstream documentation:
- http://docs.micropython.org/en/v1.9.2/pyboard/library/index.html
- http://docs.micropython.org/en/v1.9.2/pyboard/reference/index.html


## Datasheets

### MMA8653FC Accelerometer

- Product Page:
  https://www.nxp.com/products/sensors/motion-sensors/3-axis/2g-4g-8g-low-g-10-bit-digital-accelerometer:MMA8653FC
- Datasheet: https://www.nxp.com/docs/en/data-sheet/MMA8653FC.pdf

### Microcontroller

**Note**: You will NOT need to look into this datasheet to complete the
workshop, it is here only for additional information.

- Product Page:
  https://www.nordicsemi.com/Products/Low-power-short-range-wireless/nRF51822
- Product Specification:
  https://infocenter.nordicsemi.com/pdf/nRF51822_PS_v3.1.pdf
- nRF51 Series Reference Manual (datasheet):
  https://infocenter.nordicsemi.com/pdf/nRF51_RM_v3.0.pdf


## Troubleshooting

### Mu

#### REPL doesn't work

If you are on Windows 7 or 8 you will need to install this driver:
https://os.mbed.com/docs/mbed-os/v5.13/tutorials/windows-serial-driver.html

If you are on Linux, you might have to add yourself to the correct permissions
group (usually the `dialout` or `uucp` groups).

#### Cannot flash the micro:bit

If you are on Linux, make sure the MICROBIT drive is mounter. If your
distribution doesn't mount the drive automatically you might have to manually
mount it.

### Online Python Editor

WebUSB is not is necessary to complete the workshop, is a lot more convenient
and quicker.

You can still access the REPL with any serial terminal in your computer and
program the micro:bit by downloading the hex file from the Online Editor and
copying it into the MICROBIT drive.

#### It says WebUSB is not supported

You will need to use Chrome (or a Chromium based browser) for WebUSB support.

#### When I try to connect to the device it gives me an error

Make sure the micro:bit firmware is at version 0249 or newer. Follow the
instructions from this page to update the micro:bit firmware:
https://microbit.org/guide/firmware/

#### It still cannot connect via WebUSB

Follow the troubleshooting section from this micro:bit support article:
https://support.microbit.org/support/solutions/articles/19000084059-beta-testing-web-usb#troubleShooting
