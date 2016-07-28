from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^home/$', views.home, name='home'),
	url(r'^logout/$', views.logout, name="logout"),
	url(r'^process/$', views.process, name="process"),
]