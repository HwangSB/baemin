from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length = 50)
    store=models.CharField(max_length = 50)
    menu=models.CharField(max_length = 50)
    option=models.TextField()
    price=models.IntegerField()

    def __str__(self):
        return self.name+":"+self.menu