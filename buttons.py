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
joyX = gp.Button(joyXpin)
joyY = gp.Button(joyYpin)

# Global variables
switchState = 0
changingMode = False
mode = 1
emojiCount = 1

# Function definitions
def button_callback():
    global emojiCount

    if mode is 1:
        print('❀ ' * emojiCount)
    elif mode is 2:
        print('☂ ' * emojiCount)
    elif mode is 3:
        print('☃ ' * emojiCount)

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

def joyX_callback():
    global emojiCount
    
    if emojiCount > 1:
        emojiCount -= 1
    print('emoji count is ' + str(emojiCount))

def joyY_callback():
    global emojiCount

    emojiCount += 1
    print('emoji count is ' + str(emojiCount))

# Set up instructions
print('Instructions')
print("\t- To print emojis: press the button\n\t- To change modes: flip the switch to turn 'change mode' on.\n\t    Push the button to cycle through modes.\n\t    Flip the switch again to turn 'change mode' off\n\t- To increase emoji count: push joystick up in Y direction\n\t- To decrease emoji count: push joystick to the left in X direction\n")

# Main loop
while True:
    switch.when_held = switch_callback
    switch.when_released = switch_callback
    joyX.when_pressed = joyX_callback
    joyY.when_pressed = joyY_callback

    if changingMode:
        button.when_pressed = inc_mode
    else:
        button.when_pressed = button_callback

