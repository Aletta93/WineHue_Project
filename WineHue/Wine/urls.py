from django.conf.urls import url

from . import views

app_name = "Wine"
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^/wine-detail/$', views.DetailView.as_view(), name='wine-detail')
]