#!/usr/bin/python3
import os
import gpiozero as gp
import time

# Uses BCM pin numbering
buttonPin = 4
switchPin = 18
joyXpin = 22
joyYpin = 23

button = gp.Button(buttonPin)
switch = gp.Button(switchPin)
joyX = gp.Button(joyXpin)
joyY = gp.Button(joyYpin)

# Global variables
switchState = 0
changingMode = False
modeCount = 1
currX = 0
currY = 0

# Function definitions
def button_callback():
    print("Button was pushed!")

def switch_callback():
    global switchState
    global changingMode

    switchState = not switchState
    changingMode = not changingMode
    if changingMode:
        print('\n----------')
        print('CHANGE MODE ON')
        print('----------\n')
        print('Current state: ' + str(modeCount))
    else:
        print('\n----------')
        print('CHANGE MODE OFF')
        print('----------\n')

def inc_mode():
    global modeCount
    modeCount += 1
    if modeCount > 3:
        modeCount = modeCount%3
    print("Now in state: " + str(modeCount))

def joyX_callback():
    print('joy called')
    sleep(500)

def joyY_callback():
    print('yyyy')
    sleep(500)

# Main loop
while True:
    if joyX.value is 1:
        joyX_callback()
    if joyY.value is 1:
        joyY_callback()

    #print(joyX.value)
    #print(joyY.value)
    switch.when_pressed = switch_callback
    switch.when_released = switch_callback

    if changingMode:
        button.when_pressed = inc_mode
    else:
        button.when_pressed = button_callback
