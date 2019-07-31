from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=30)
    bank_id = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)


