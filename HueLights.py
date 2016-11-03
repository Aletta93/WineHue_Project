from phue import Bridge
import time
import sys
import colorsys
from math import floor

ip = '10.0.0.4'


connect = False
try:
	b = Bridge(ip)
	connect = True
	print("Connection to bridge sucessfull")
except ConnectionError:
	print("Could not connect to hue bridge.")
	print("Waiting for pairing button to be pressed.")

while not connect:
	try:
		b = Bridge(ip)
		print("\nConnection to bridge sucessfull")
		connect = True
	except ConnectionError:
		print(".", end='')
		sys.stdout.flush()
		time.sleep(1)

lights = b.lights

red = 0
green = 255
blue = 0

red = red/255
green = green/255
blue = blue/255

if red > 0.04045:
	red = ((red + 0.055)/(1.0 + 0.055)) ** 2.4
else: 
	red = red / 12.92

if green > 0.04045:
	green = ((green + 0.055)/(1.0 + 0.055)) ** 2.4
else: 
	green = green / 12.92

if blue > 0.04045:
	blue = ((blue + 0.055)/(1.0 + 0.055)) ** 2.4
else: 
	blue = blue / 12.92

X = red * 0.664511 + green * 0.154324 + blue * 0.162028
Y = red * 0.283881 + green * 0.668433 + blue * 0.047685
Z = red * 0.000088 + green * 0.072310 + blue * 0.986039

lights[0].on = True
lights[0].brightness = floor(Y * 254)

lights[1].on = True
lights[1].brightness = floor(Y * 254)

x = X / (X + Y + Z)
y = Y / (X + Y + Z)

lights[0].transmitiontime = 300

lights[0].xy = [x, y]
lights[1].xy = [x, y]


lights[0].brightness = 0