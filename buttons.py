#!/usr/bin/python3
import os
import gpiozero as gp
import time

# Uses BCM pin numbering
buttonPin = 4
switchPin = 24
joyXpin = 22
joyYpin = 23

button = gp.Button(buttonPin)
switch = gp.Button(switchPin)
joyX = gp.Button(switchPin)
joyY = gp.Button(switchPin)

# Global variables
switchState = 0
changingMode = False
mode = 1
emojiCount = 1

# Function definitions
def button_callback():
    global emojiCount

    if mode is 1:
        print('❀' * emojiCount)
    elif mode is 2:
        print('☂' * emojiCount)
    elif mode is 3:
        print('☃' * emojiCount)

def switch_callback():
    global switchState
    global changingMode

    switchState = not switchState
    changingMode = not changingMode

    if changingMode:
        print('\n----------')
        print('CHANGE MODE ON')
        print('----------\n')
        print('Current mode: ' + str(mode))
    else:
        print('\n----------')
        print('CHANGE MODE OFF')
        print('----------\n')

    if joyX.value is 1:
        emojiCount += 1
    # elif joyY.value is 1:
    #     emojiCount -= 1

def inc_mode():
    global mode
    mode += 1
    if mode > 3:
        mode = mode%3

    # Print funny mode names
    if mode is 1:
        print('1: Flower Power Mode')
    elif mode is 2:
        print('2: Rainy Day Mode')
    elif mode is 3:
        print('3: Winter is Coming')

# Main loop
while True:
    switch.when_held = switch_callback
    switch.when_released = switch_callback

    if changingMode:
        button.when_pressed = inc_mode
    else:
        button.when_pressed = button_callback
