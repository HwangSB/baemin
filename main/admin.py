from django.contrib import admin
from .models import Item
from .models import User
# Register your models here.
admin.site.register(Item)
admin.site.register(User)