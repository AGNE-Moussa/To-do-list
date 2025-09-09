from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email  = models.EmailField(unique = True)
    password = models.CharField(max_length = 100)
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    titre = models.CharField(max_length = 200)
    description = models.TextField()
    completed = models.BooleanField(default = False)
    createad_at= models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)


