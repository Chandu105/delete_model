from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=100)
    cid=models.IntegerField()
    