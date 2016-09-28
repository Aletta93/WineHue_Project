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
