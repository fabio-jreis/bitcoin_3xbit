from django.db import models

# Create your models here.
class BtcDeposit(models.Model):
    addr = models.CharField(max_length=40)

    @staticmethod
    def save(x):
     BtcDeposit.addr = x

