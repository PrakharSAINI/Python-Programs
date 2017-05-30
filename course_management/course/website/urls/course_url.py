from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from website.views import login,register

urlpatterns = [
    url(r'^register$',TemplateView.as_view(template_name="website/registerscreen.html"),name="register-pg"),
    url(r'^login$',TemplateView.as_view(template_name="website/loginscreen.html"),name="login-pg"),
    url(r'^registering$',register,name="register-usr"),
    url(r'^logging$',login,name="rlogin-usr"),
    url(r'^exists$',TemplateView.as_view(template_name="website/mainscreen.html"),name="work-area"),
]
