from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Site(models.Model):
	name = models.CharField(max_length=64)
	ip_address = models.CharField(max_length=16, blank=True)
	username = models.CharField(max_length=50, blank=True)
	password = models.CharField(max_length=100, blank=True)
    
	def __str__(self):
		return f"{self.name}"

