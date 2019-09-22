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

def button_callback(channel):
    print("Button was pushed!")

switchState = 0
changingMode = False
modeCount = 1

def switch_callback(channel):
    global switchState
    global changingMode

    switchState = not switchState
    changingMode = not changingMode
    if changingMode:
        print('CHANGE MODE ON')
        print('----------\n')
        print('Current state: ' + str(modeCount))
    else:
        print('\n----------')
        print('CHANGE MODE OFF\n')

def inc_mode(channel):
    global modeCount
    modeCount += 1
    if modeCount > 3:
        modeCount = modeCount%3
    print("Now in state: " + str(modeCount))

input('Press Enter to quit: \n\n')

while True:
    switch.when_pressed = switch_callback
    switch.when_released = switch_callback

    if changingMode:
        button.when_pressed = inc_mode
    else:
        button.when_pressed = button_callback

# firstCall = True
# prevState = 0
# lastDebounce = 0.
# debounceDelay = 250.
#

#
# def joyx_callback(channel):
#     print('xxxxxx: ', GPIO.input(channel))
#
# def joyy_callback(channel):
#     print('yyyyyyy: ', GPIO.input(channel))
#
# def switch_callback(channel):
#     global firstCall
#     global prevState
#     if firstCall:
#         prevState = GPIO.input(channel)
#         firstCall = False
#
#     newInput = GPIO.input(channel)
#    # print(newInput, prevState)
#     if (newInput is not prevState):
#         print('switched')
#     prevState = newInput
#
# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.setup(joyX, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(joyY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.add_event_detect(buttonPin,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
# GPIO.add_event_detect(joyX,GPIO.BOTH,callback=joyx_callback)
# GPIO.add_event_detect(joyY,GPIO.BOTH,callback=joyy_callback)
# GPIO.add_event_detect(switchPin,GPIO.BOTH,callback=switch_callback)
#
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up
