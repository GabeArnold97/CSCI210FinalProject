# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Division(models.Model):
	name = models.CharField(max_length=100)
	picture = models.CharField(max_length=300, default='')
	def __unicode__(self):
		return unicode(self.name)
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, default=1)
    titles = models.CharField(max_length=100)
    picture = models.CharField(max_length=300, default='')
    def __unicode(self):
        return unicode(self.name)