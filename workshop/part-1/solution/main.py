from microbit import display, button_a, Image, accelerometer, sleep

display.scroll('Hello World!')
display.show(Image.HAPPY)
sleep(1000)

while True:
    if button_a.is_pressed():
        display.show(Image.HOUSE)
        sleep(1000)

    if accelerometer.was_gesture('shake'):
        print('hey')
        display.show(Image.HAPPY)
        sleep(1000)

    display.clear()
