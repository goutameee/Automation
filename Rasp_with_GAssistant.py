import os
import logging
import argparse
import json
import socket
import RPi.GPIO as GPIO

import google.auth.transport.grpc
import google.auth.transport.requests
import google.oauth2.credentials

import google_assistant_library_helpers
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

logging.basicConfig(level=logging.DEBUG)

# Define the GPIO pins for the home appliances
LIGHT_PIN = 17
FAN_PIN = 27

# Define the commands to control home appliances
COMMANDS = {
    "turn on the light": "light_on",
    "turn off the light": "light_off",
    "turn on the fan": "fan_on",
    "turn off the fan": "fan_off",
    # Add additional commands here
}

# Define a function to run a command
def run_command(command):
    if command == "light_on":
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
    elif command == "light_off":
        GPIO.output(LIGHT_PIN, GPIO.LOW)
    elif command == "fan_on":
        GPIO.output(FAN_PIN, GPIO.HIGH)
    elif command == "fan_off":
        GPIO.output(FAN_PIN, GPIO.LOW)

# Define the callback for processing events
def process_event(event):
    # Check if the event is a new conversation
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print("Conversation started!")
        
    # Check if the event is a conversation end
    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        print("Conversation ended!")
    
    # Check if the event is a new audio request
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        text = event.args["text"].lower()
        print("You said: " + text)
        
        # Check if the text matches a command
        for command in COMMANDS:
            if command in text:
                run_command(COMMANDS[command])

# Main program loop
def main():
    # Set up the GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.setup(FAN_PIN, GPIO.OUT)
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    
    # Load the OAuth2 credentials
    try:
        with open(args.credentials, 'r') as f:
            credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(
                json.loads(f.read())
            )
    except Exception as e:
        logging.error('Error loading credentials: %s', e)
        logging.error('Run google-oauthlib-tool to initialize '
                      'new OAuth2 credentials.')
        return
    
    # Connect to the Google Assistant API
    device_config = google_assistant_library_helpers.DeviceConfig()
    with Assistant(credentials, device_config) as assistant:
        for event in assistant.start():
            process_event(event)

if __name__ == '__main__':
    main()
