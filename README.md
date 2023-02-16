# Automation
This is a repository where codes are stored that are needed to automate our bulky tasks.
The two codes have a similar purpose, which is to control home appliances using voice commands received through a Google Home device or the Google Assistant app. However, the difference lies in the technology used to communicate with the appliances.

The first code uses the Google Assistant SDK, which communicates with the Google Home device or the Google Assistant app through the internet. The SDK sends voice commands to a server, which interprets the commands and sends back the appropriate response to the device. The response is then used to control the appliances.

The second code uses both the Google Assistant SDK and the RPi.GPIO library, which communicates directly with the Raspberry Pi's General Purpose Input/Output (GPIO) pins. This means that the Raspberry Pi can directly control the appliances connected to its GPIO pins without the need for a separate internet connection or server. This can be useful for controlling appliances that are physically connected to the Raspberry Pi, such as lights or fans.
