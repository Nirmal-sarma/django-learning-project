from django.db import models

# Create your models here.
# model are responsible for interacting with database without writing sql code 

class Feature:
    id : int
    name: str
    details: str
