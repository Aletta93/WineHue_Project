from phue import Bridge
import time
import sys
import colorsys

ip = '10.0.0.12'
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

rgb = [127, 0, 127]

rgb[0] = rgb[0]/254
rgb[1] = rgb[1]/254
rgb[2] = rgb[2]/254

lights[0].on = True
lights[0].brightness = 60

r = rgb[0] / (rgb[0] + rgb[1] + rgb[2])
g = rgb[1] / (rgb[0] + rgb[1] + rgb[2])

lights[0].xy = [r, g]
