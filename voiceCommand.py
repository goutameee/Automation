import speech_recognition as sr
import os

# Set up the recognizer
r = sr.Recognizer()

# Set up the microphone
mic = sr.Microphone()

# Define a function to turn on the machine
def turn_on_machine():
    # Replace the command here with the command to turn on your machine
    os.system("echo 'turn on machine'")

# Main program loop
while True:
    # Listen for a command
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        
    # Use Google's speech recognition service to transcribe the command
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        
        # Check if the command is to turn on the machine
        if "turn on the machine" in command:
            turn_on_machine()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
