from django.conf.urls import url

from . import views

app_name = "Wine"
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^wine-list/$', views.WineListView.as_view(), name='wine-list'),
	url(r'^(?P<pk>[0-9]+)/wine-detail/$', views.WineView.as_view(), name='wine-detail'),
	url(r'^(?P<wine_id>[0-9]+)/selection/$', views.wine_select, name='select')
]