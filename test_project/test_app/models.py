from django.db import models
from datetime import datetime

# Create your models here.
class Features(models.Model):
    
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    current_time = models.DateTimeField(default=datetime.now , blank=True)
    
    