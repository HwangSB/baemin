from django.contrib import admin
from .models import Store
from .models import User
# Register your models here.
admin.site.register(Store)
admin.site.register(User)