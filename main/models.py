from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, default='')
    menu = models.TextField()

    def __str__(self):
        return self.name + " >> " + self.menu

class User(models.Model):
    store = models.CharField(max_length = 50, default='')
    menu = models.CharField(max_length = 50, default='')
    option = models.TextField(default='option')
    price = models.IntegerField()

    def __str__(self):
        return self.store + " >> " + self.menu