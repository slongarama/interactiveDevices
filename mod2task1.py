#!/usr/bin/python3

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

button_pin = 7
switch_pin = 18
joy_pin_x = 15
joy_pin_y = 16

firstCall = True
prevState = 0
lastDebounce = 0.
debounceDelay = 250.

def button_callback(channel):
    global lastDebounce
    if (time.time() * 1000. - lastDebounce > debounceDelay):
        print("Button was pushed!")
        lastDebounce = 1000. * time.time()

def joyx_callback(channel):
    print('xxxxxx: ', GPIO.input(channel))

def joyy_callback(channel):
    print('yyyyyyy: ', GPIO.input(channel))

def switch_callback(channel):
    global firstCall
    global prevState
    if firstCall:
        prevState = GPIO.input(channel)
        firstCall = False

    newInput = GPIO.input(channel)
   # print(newInput, prevState)
    if (newInput is not prevState):
        print('switched')
    prevState = newInput

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(joy_pin_x, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(joy_pin_y, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(joy_pin_x,GPIO.BOTH,callback=joyx_callback)
GPIO.add_event_detect(joy_pin_y,GPIO.BOTH,callback=joyy_callback)
GPIO.add_event_detect(switch_pin,GPIO.BOTH,callback=switch_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up


