from django.db import models

# Create your models here.
# model are responsible for interacting with database without writing sql code 

class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    icon=models.CharField(max_length=100,null=True)
    
