from django.db import models

# Create your models here.
class Deposits(models.Model):
    address = models.CharField(max_length=40, null=False, blank=False) 
    key =  models.CharField(max_length=40, null=False, blank=False) 
    objetos = models.Manager()  