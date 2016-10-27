from phue import Bridge
import time
import sys
import colorsys

ip = '10.0.0.3'

def Connect_bridge(ip):
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

	return b.lights

def Change_colour(red,green,blue,lights):

	red = red/254
	green = green/254
	blue = blue/254

	lights[0].on = True
	lights[0].brightness = 60

	r = red / (red + green + blue)
	g = green / (red + green + blue)

	lights[0].xy = [r, g]
	lights[1].xy = [r, g]

