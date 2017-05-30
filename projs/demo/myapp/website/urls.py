from django.conf.urls import url
from website.views import index, login

urlpatterns = [
	url(r'^login/$', login)	,
	url(r'^$', index),
	url(r'^index/$', index),
	url(r'^home/$', index)
]