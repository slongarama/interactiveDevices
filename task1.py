#!/usr/bin/python3
import gpiozero as gp
import time

# Uses BCM pin numbering
buttonPin = 4
switchPin = 24
joyX = 22
joyY = 23

button = gp.Button(buttonPin)
switch = gp.Button(switchPin)

# Global variables
switchState = 0
changingMode = False
modeCount = 1

def button_callback(channel):
    print("Button was pushed!")


def switch_callback(channel):
    switchState = not switchState
    print(switchState)

def inc_mode(channel):
    global modeCount
    modeCount += 1
    if modeCount > 3:
        modeCount = modeCount%3 + 1
    print("Now in state: " + str(modeCount))

while True:
    switch.when_pressed = switch_callback
    switch.when_released = switch_callback

    if changingMode:
        button.when_pressed = inc_mode
    else:
        button.when_pressed = button_callback
