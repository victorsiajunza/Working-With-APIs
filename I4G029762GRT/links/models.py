from os import link
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class links(models.Model):
 link


target_url : models.URLField(max_length=200)

 

description : models.CharField(max_length=200)

 

identifier: models.SlugField(max_length=20 blank=True,unique=True)

 

author : models.ForeignKey(get_user_model())

 

created_date : A date-time column, use Django’s models.DateTimeField.