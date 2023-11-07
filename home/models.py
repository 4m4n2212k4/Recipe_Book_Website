from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class NewBlog(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    dish = models.TextField()
    Ingredients = models.TextField()
    Recipe = models.TextField() 
    date = models.DateField()


    def __str__(self):
        return self.name