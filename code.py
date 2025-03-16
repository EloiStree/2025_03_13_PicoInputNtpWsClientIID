import sys
print("Hello World APInt IO Listener only for Pico Wifi")
print("NOTE: Pico has one core, thread. You can only listen or send data, not both at the same time.")
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

# print ("Gamepad is ready, creation of RSA")
# key_info= "n:7678474498829357529896573097481858575053585872007675919829553419296214907977828182640077413970894795848746422705861825126769530253533522069338216935925251,d:494776962762353736801398113900024242221207762599576047262465539919250431442030408007194995154195563816134112307588370930204511748465693656142690187437321,p:7334601364267231523356176037758493097799589942874861181457753999892004415195138327,q:1046883684263661531990802385218273050697844155933076191572876428590401013,e:65537"    
# rsa = RSASignature512PicoW(key_info, key_size=512)
# rsa.test("Hello World")


ws_url = "ws://apint.ddns.net:4615"
udp_gate_ipv4 = "apint.local"
udp_gate_port =3620
udp_gate_listen_port = 3621




    
def try_to_connect_wifi():
    """Connect to Wi-Fi using the credentials defined in setting.toml """
    
    WIFI_SSID = os.getenv("WIFI_SSID")
    WIFI_PASSWORD = os.getenv("WIFI_PASSWORD")
    print(f"WIFI_SSID: {WIFI_SSID}")
    print("Connecting to Wi-Fi...")
    try:
        wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
        print("Connected to Wi-Fi!")
    except ConnectionError as e:
        print("Failed to connect to Wi-Fi:", e)
        raise e
    
    time.sleep(1)
    print("Ready to play World of Warcraft from Pico Wifi !")
    print('Pico Wifi IP address is:', wifi.radio.ipv4_address)
    
try_to_connect_wifi()


target_address = (udp_gate_ipv4, udp_gate_port)

def send_index_integer(index:int,integer:int):
        byte_integer_value = struct.pack("<ii", index,integer)
        pool = socketpool.SocketPool(wifi.radio)
        udp_socket = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
        #try:
        udp_socket.sendto(byte_integer_value, target_address)
        print(f"Sent II: {index} {integer} to {udp_gate_ipv4}:{udp_gate_port}")
       # except:
       #     print(f"Failed to send II: {index} {integer} to {self.m_ip_target}:{self.m_port_byte_integer}")
        
       # finally:
        udp_socket.close()

def udp_sender():
    value = 0
    index=0
    while True:
        send_index_integer(index,value)
        value += 1
        time.sleep(1)

def udp_listener():
    print("my IP addr:", wifi.radio.ipv4_address)
    pool = socketpool.SocketPool(wifi.radio)
    udp_buffer = bytearray(64)  
    sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM) 
    sock.bind(("0.0.0.0", udp_gate_listen_port))  

    print("waiting for packets on","0.0.0.0", udp_gate_listen_port)
    while True:
        size, addr = sock.recvfrom_into(udp_buffer)
        print(f"Received message from {addr[0]}|{size}:", udp_buffer[:size])
        
        if size == 4:
            integer = struct.unpack("<i", udp_buffer[:size])[0]
            print(f"Received integer: {integer}")
        elif size == 8:
            index, integer = struct.unpack("<ii", udp_buffer[:size])
            print(f"Received index: {index} integer: {integer}")
        elif size == 12:
            integer, timestamp = struct.unpack("<iq", udp_buffer[:size])
            print(f"Received integer: {integer} timestamp: {timestamp}")
        elif size == 16:
            index, integer, timestamp = struct.unpack("<iiq", udp_buffer[:size])
            print(f"Received index: {index} integer: {integer} timestamp: {timestamp}")
            
       
# Run the UDP listener

send_index_integer(80085, 42)
udp_listener()
