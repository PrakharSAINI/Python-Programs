from django.shortcuts import render
import json
from website.models import AuthUser
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404, HttpResponse


# Create your views here.

@csrf_exempt
def register(request):
	name=request.POST.get('user_name')
	email=request.POST.get('user_email')
	passwrd = request.POST.get('user_pass')

	new_usr = AuthUser()
	new_usr.email = email
	new_usr.password = passwrd
	new_usr.is_superuser = 0
	new_usr.first_name=name
	new_usr.last_name=' '
	new_usr.date_joined = '2017-04-27'
	new_usr.is_staff = 0
	new_usr.is_active = 1
	new_usr.save()

	return HttpResponse("registered")

@csrf_exempt
def login(request):
	output = []
	email=request.GET.get('email')
	passwrd = request.GET.get('password')
	print email
	print passwrd
	obj=AuthUser.objects.get(email=email)
	if(obj.password == passwrd):
		output['status'] = 'SUCCESS'
		output['message'] = 'login successfull'
	else:
		output['status'] = 'INVALID'
		output['message'] = 'invalid credentials'


	return HttpResponse(json.dumps(output), content_type='application/json')
