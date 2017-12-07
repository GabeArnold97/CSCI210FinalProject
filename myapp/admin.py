# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import *

# Register your models here.

class DivisionAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'division', 'titles',)

admin.site.register(Division, DivisionAdmin)
admin.site.register(Team, TeamAdmin)