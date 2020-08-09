"""baemin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('update.html/<int:store_id>',views.update,name='update1'),
    path('menu/<int:store_id>', views.menu, name='menu'),
    path('product/<int:store_id>/<int:menu_id>',views.product,name='product'),
    path('payment/',views.payment,name='payment'),


    path('create_item/',views.create_item,name='create_item'),
    path('update_item/<int:item_id>',views.update_item,name='update_item'),
    path('delete_item/<int:item_id>',views.delete_item,name='delete_item'),

    path('create_user/',views.create_user,name='create_user'),
    path('update_user/<int:item_id>',views.update_user,name='update_user'),
    path('delete_user/<int:item_id>',views.delete_user,name='delete_user'),
]
