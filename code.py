import sys
print("Hello World")
print(f"sys.implementation: {sys.implementation}")
print(f"sys.version: {sys.version}")
print(f"sys.platform: {sys.platform}")



import time
import board
import busio
import pulseio
import analogio
import random
import struct
import digitalio
import usb_hid
import usb_midi
import adafruit_midi
import time
import ssl
import socketpool
import wifi
import adafruit_requests
import os
import ipaddress


# IMPORT FROM NEAR FILE
from hid_gamepad import Gamepad
from wow_int import WowInt
from hc_ttl import HCTTL
from bluetooth_electronics_builder import BluetoothElectronicsBuilder

# IMPORT FROM LIB ADAFRUIT
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#from keyboard_layout_fr import KeyboardLayoutFR  # Import the French layout
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode



# 🐿️ If gamepad is not found in usb_hid.devices
# Just reboot the device in boot mode and comeback.
gamepad= Gamepad(usb_hid.devices)           # Start behaving as gamepad
mouse  = Mouse(usb_hid.devices)             # Start behaving as mouse
consumer = ConsumerControl(usb_hid.devices) # Start behaving as media control
keyboard = Keyboard(usb_hid.devices)
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=0, out_channel=0)



while True:

    note = random.randint(30, 90)  # Choose a random MIDI note
    velocity = random.randint(50, 127)  # Random velocity
    print(f"Sending Note On: {note}, Velocity: {velocity}")
    midi.send(NoteOn(note, velocity))  # Send Note On
    time.sleep(1)  # Hold the note for a short time

    print(f"Sending Note Off: {note}")
    midi.send(NoteOff(note, 0))  # Send Note Off
    time.sleep(1)  # Wait 1 second before the next note

