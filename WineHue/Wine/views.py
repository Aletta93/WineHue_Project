from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .HueLights import Connect_bridge, Change_colour  

from .models import Flavour, Wine_Detail

class IndexView(generic.ListView):
	template_name ='Wine/index.html'
	context_object_name = 'wine_list'

	def get_queryset(self):
		try:
			lights = Connect_bridge(settings.BRIDGE_IP)
			Change_colour(
				0,
				0,
				100,
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
			Change_colour(
				254,
				190,
				79,
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
	flavour = Flavour.objects.all()

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
		})
