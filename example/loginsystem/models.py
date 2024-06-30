from django.db import models

# Create your models here.


class usersignin(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    pass1=models.CharField( max_length=50)
    pass2=models.CharField( max_length=50)    