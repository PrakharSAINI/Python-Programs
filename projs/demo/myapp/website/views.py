from django.shortcuts import render
import json
from annoying.decorators import render_to
# Create your views here.

from django.http import HttpResponse

@render_to("website/index.html")
def index(request):
	msg = {"status": "SUCCESS", "msg": "This worked !!!"}
	#return HttpResponse("This is simple response")
	#return HttpResponse(json.dumps(msg), content_type='application/json')
	return {}

@render_to("website/login.html")
def login(request):
	return {}