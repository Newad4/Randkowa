from django.db import models

# Create your models here.

class Gender(models.Model):
    value = models.CharField(max_length=32)
class Profil(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    age = models.IntegerField()
    description = models.TextField()
    photos = models.ImageField(upload_to='profile_pics', blank=True)


class Choices(models.Model):
    name = models.CharField(max_length=32)

