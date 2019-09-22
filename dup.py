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

def button_callback(channel):
    print("Button was pushed!")

state = 0

def switch_callback(channel):
    state = not state
    print(state)

while True:
    button.when_pressed = button_callback
    switch.when_pressed = switch_callback


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
