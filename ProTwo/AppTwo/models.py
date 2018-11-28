from django.db import models

class User(models.Model):
    """Database for user information"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name, self.last_name, self.email 
# Create your models here.
