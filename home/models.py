from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=300)

    def __str__(self):
        return self.name