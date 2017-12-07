# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *
import re

# Create your views here.



def home(request):
	teams = Team.objects.all()
	t = loader.get_template('home.html')
	c = dict({'teams': teams})
	return HttpResponse(t.render(c))
	
def team(request, name):
	teams = Team.objects.filter(name=name)
	t = loader.get_template('team.html')
	c = dict({'teamSelect': teams})
	return HttpResponse(t.render(c))

def division(request, name):
    divisionname = str(re.sub('/division/', '', (request.path)))
    divisionobj = Division.objects.get(name=divisionname)
    teams = Team.objects.filter(division_id=divisionobj.id)
    divisions = Division.objects.filter(name=name)
    t = loader.get_template('division.html')
    c = dict({'divisionSelect': divisions, 'teamSelect': teams})
    return HttpResponse(t.render(c))