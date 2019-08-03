from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=300)
    bank_id = models.CharField(max_length=300)
    branch = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    bank_name = models.CharField(max_length=500)