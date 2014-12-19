''' -- imports from installed packages -- '''
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django_mongokit import get_database

try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId


# Create your views here.

def homepage(request):	

	return render_to_response("home.html",context_instance=RequestContext(request))
