from django.db import models
# class feature:
#     id:int
#     name:str
#     details:str
# Create your models here.
class feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
