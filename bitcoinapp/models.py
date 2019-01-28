from django.db import models

# Create your models here.
class BtcDeposit(object):
    addr = ''

    @staticmethod
    def save(x):
     BtcDeposit.addr = x

