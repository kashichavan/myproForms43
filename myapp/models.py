from django.db import models


gender_choice=[
    ('male','MALE'),
    ('female','FEMALE'),
    ('others','OTHERS'),
]
# Create your models here.
class Register(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(choices=gender_choice,max_length=30,default='MALE')


