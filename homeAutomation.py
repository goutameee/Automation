# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Define a function to turn on/off lights
def lights(status):
    if status == 'on':
        GPIO.output(7, GPIO.HIGH)
        print("Lights turned on")
    else:
        GPIO.output(7, GPIO.LOW)
        print("Lights turned off")

# Define a function to lock/unlock doors
def doors(status):
    if status == 'lock':
        GPIO.output(11, GPIO.HIGH)
        print("Doors locked")
    else:
        GPIO.output(11, GPIO.LOW)
        print("Doors unlocked")

# Define a function to turn on/off TV
def tv(status):
    if status == 'on':
        GPIO.output(13, GPIO.HIGH)
        print("TV turned on")
    else:
        GPIO.output(13, GPIO.LOW)
        print("TV turned off")

# Define a function to turn on/off fan
def fan(status):
    if status == 'on':
        GPIO.output(15, GPIO.HIGH)
        print("Fan turned on")
    else:
        GPIO.output(15, GPIO.LOW)
        print("Fan turned off")

# Main program loop
while True:
    command = input("Enter command (e.g. 'lights on', 'doors unlock'): ")
    command_parts = command.split()
    if len(command_parts) == 2:
        device = command_parts[0]
        action = command_parts[1]
        if device == 'lights':
            lights(action)
        elif device == 'doors':
            doors(action)
        elif device == 'tv':
            tv(action)
        elif device == 'fan':
            fan(action)
    else:
        print("Invalid command")
