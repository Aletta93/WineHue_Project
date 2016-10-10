from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Wine_Detail

class IndexView(generic.ListView):
	template_name ='Wine/index.html'
	context_object_name = 'wine_list'

	def get_queryset(self):
		return Wine_Detail.objects.all()

class WineListView(generic.ListView):
	template_name ='Wine/wine-list.html'
	context_object_name = 'wine_list'

	def get_queryset(self):
		return Wine_Detail.objects.all()

class WineView(generic.DetailView):
	model = Wine_Detail
	template_name = 'Wine/detail.html'

def wine_select(request, wine_id):
	selection = get_object_or_404(Wine_Detail, pk=wine_id)
	return render(request, 'Wine/detail.html', {
		'selection':selection,
		})
