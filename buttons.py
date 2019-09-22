#!/usr/bin/python3

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

currState = 0
switchState = 1
lastDebounce = 0.
debounceDelay = 250.

def button_callback(channel):
    global lastDebounce
    if (time.time() * 1000. - lastDebounce > debounceDelay):
        print("Button was pushed!")
        lastDebounce = 1000. * time.time()

def joyx_callback(channel):
    print('xxxxxx')

def joyy_callback(channel):
    print('yyyyyyy')
    print(channel)

def switch_callback(channel):
    global switchState
    global currState
    print(currState, switchState)
    currState = GPIO.input(channel)
    if currState != switchState:
        print('switched!')
        switchState=currState

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(15,GPIO.RISING,callback=joyx_callback)
GPIO.add_event_detect(16,GPIO.RISING,callback=joyy_callback)
GPIO.add_event_detect(18,GPIO.RISING,callback=switch_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up


