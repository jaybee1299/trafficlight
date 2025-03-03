import serial
import time
from whisper_mic import WhisperMic

# Specify the COM port and baud rate for the connection to Arduino
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the port your Arduino is connected to
time.sleep(2)  # Allow time for Arduino to reset

# Function to control LEDs based on command
def control_led(led_number):
    if led_number == 1:
        ser.write(b'1')  # Command to turn on LED 1 (Friday)
        print("LED 1 (Friday) turned ON")
    elif led_number == 2:
        ser.write(b'2')  # Command to turn on LED 2 (Saturday)
        print("LED 2 (Saturday) turned ON")
    elif led_number == 3:
        ser.write(b'3')  # Command to turn on LED 3 (Sunday)
        print("LED 3 (Sunday) turned ON")
    elif led_number == 0:
        ser.write(b'0')  # Command to turn off all LEDs
        print("All LEDs turned OFF")
    elif led_number == 4:
        # Turn on all LEDs for weekend (Friday, Saturday, Sunday)
        ser.write(b'1')
        ser.write(b'2')
        ser.write(b'3')
        print("All LEDs turned ON (Weekend)")
    else:
        print("Invalid LED number!")

# Create an instance of WhisperMic for live voice recognition
mic = WhisperMic()

# Keywords for control (can be extended)
keywords = ["friday", "saturday", "sunday", "off", "turn off", "weekend"]

# Main loop to listen for voice commands and control LEDs
while True:
    print("Listening for voice command...")

    # Listen to the microphone and get the transcribed result
    result = mic.listen()  # Listen for the voice command
    print(f"Recognized text: {result}")

    # Convert the transcribed text to lowercase for case-insensitive matching
    result = result.lower()

    # Check for the presence of the keywords in the transcribed result
    detected_keywords = [word for word in keywords if word.lower() in result]

    if detected_keywords:
        print("Detected Keywords: ", detected_keywords)
        
        # Control LEDs based on the detected keywords
        if 'friday' in detected_keywords:
            control_led(1)  # Control LED for Friday
        elif 'saturday' in detected_keywords:
            control_led(2)  # Control LED for Saturday
        elif 'sunday' in detected_keywords:
            control_led(3)  # Control LED for Sunday
        elif 'off' in detected_keywords or 'turn off' in detected_keywords:
            control_led(0)  # Turn off all LEDs
        elif 'weekend' in detected_keywords:
            control_led(4)  # Turn on all LEDs for the weekend
    else:
        print("No relevant keywords detected.")
