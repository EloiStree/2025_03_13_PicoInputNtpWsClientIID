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

import time
import board
import wifi
import socketpool
import adafruit_requests
import json
import wifi
import time
import hashlib
import wifi
import socketpool
import adafruit_wsgi as wsgi

# IMPORT FROM NEAR FILE
from hid_gamepad import Gamepad
from wow_int import WowInt
from hc_ttl import HCTTL
from bluetooth_electronics_builder import BluetoothElectronicsBuilder
from apintio import APIntIO_SHA256

# IMPORT FROM LIB ADAFRUIT
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#from keyboard_layout_fr import KeyboardLayoutFR  # Import the French layout
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from rsa_sign import RSASignature512PicoW

# 🐿️ If gamepad is not found in usb_hid.devices
# Just reboot the device in boot mode and comeback.
gamepad= Gamepad(usb_hid.devices)           # Start behaving as gamepad
mouse  = Mouse(usb_hid.devices)             # Start behaving as mouse
consumer = ConsumerControl(usb_hid.devices) # Start behaving as media control
keyboard = Keyboard(usb_hid.devices)
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], midi_out=usb_midi.ports[1], in_channel=0, out_channel=0)


key_info= "n:7678474498829357529896573097481858575053585872007675919829553419296214907977828182640077413970894795848746422705861825126769530253533522069338216935925251,d:494776962762353736801398113900024242221207762599576047262465539919250431442030408007194995154195563816134112307588370930204511748465693656142690187437321,p:7334601364267231523356176037758493097799589942874861181457753999892004415195138327,q:1046883684263661531990802385218273050697844155933076191572876428590401013,e:65537"    
rsa = RSASignature512PicoW(key_info, key_size=512)


apint = APIntIO_SHA256( "Patato",auto_launch_wifi=True)
print(f"{apint.password}:{apint.password_hash}") 


rsa.test("Hello World")
ws_url = "ws://apint.ddns.net:4615"
print("Connected to Wi-Fi!")
print("IP Address:", wifi.radio.ipv4_address)
## WAS EXPECTING THE WEBSOCKET CLIENT TO BE EASY TO CODE..
## BUT IT IS NOT.. SO I WILL USE THE HTTP CLIENT INSTEAD
## Micro Python is better design for that but it is not in circuit python


## UDP client works fine but is not design for autherntication
## HTTP should work but require APINT FLASK SERVER TO BE UP

## All that to say  I am a bit block where.

    
while True:

    note = random.randint(30, 90)  # Choose a random MIDI note
    velocity = random.randint(50, 127)  # Random velocity
    print(f"Sending Note On: {note}, Velocity: {velocity}")
    midi.send(NoteOn(note, velocity))  # Send Note On
    time.sleep(1)  # Hold the note for a short time

    print(f"Sending Note Off: {note}")
    midi.send(NoteOff(note, 0))  # Send Note Off
    time.sleep(1)  # Wait 1 second before the next note

