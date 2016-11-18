from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .HueLights import Connect_bridge, Change_colour  

from .models import Characteristic, Flavour, Wine_Detail
import random

class IndexView(generic.ListView):
	template_name ='Wine/index.html'
	context_object_name = 'wine_list'

	def get_queryset(self):
		try:
			lights = Connect_bridge(settings.BRIDGE_IP)
			r = random.random()
			red = 0
			green = 0
			blue = 0
			if r < .33:
				red = 0
				green = 0
				blue = 100
			elif r < .66:
				red = 128
				green = 0
				blue = 128
			else:
				red = 0
				green = 139
				blue = 139

			Change_colour(
				red,
				green,
				blue,
				lights
			)
		except:
			print("Coud not connect to bridge. Check IP or press bridge button.")
		return Wine_Detail.objects.all()

class WineListView(generic.ListView):
	template_name ='Wine/wine_list.html'
	context_object_name = 'wine_list'

	def get_queryset(self):
		try:
			lights = Connect_bridge(settings.BRIDGE_IP)
			r = random.random()
			print(r)
			red = 0
			green = 0
			blue = 0
			if r < .5:
				red = 0
				green = 139
				blue = 139
			else:
				red = 0
				green = 128
				blue = 0

			Change_colour(
				red,
				green,
				blue,
				lights
			)
		except:
			print("Coud not connect to bridge. Check IP or press bridge button.")
		return Wine_Detail.objects.all()



class WineView(generic.ListView):
	model = Flavour
	template_name = 'Wine/detail.html'
	context_object_name = 'flavour_list'

def wine_select(request, wine_id):
	selection = get_object_or_404(Wine_Detail, pk=wine_id)
	flavour = Flavour.objects.filter(wine_name=wine_id).order_by('-flavour_strength')
	character = Characteristic.objects.filter(wine_name=wine_id)

	# Tries to connect to the bridge in order to change the lights
	# Just prints out a message when it cant connect.
	try:
		lights = Connect_bridge(settings.BRIDGE_IP)
		Change_colour(
			selection.colour_red,
			selection.colour_green,
			selection.colour_blue,
			lights
		)
	except:
		print("Coud not connect to bridge. Check IP or press bridge button.")
	return render(request, 'Wine/detail.html', {
		'selection':selection,
		'flavours':flavour,
		'character': character,
		})