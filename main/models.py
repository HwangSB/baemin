from django.db import models

# Create your models here.
class Item(models.Model):
    usertype=models.CharField(max_length = 50, default='USER')
    store=models.CharField(max_length = 50, default='')
    menu=models.TextField()
    option=models.TextField(default='option')
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.store + " >> " + self.menu