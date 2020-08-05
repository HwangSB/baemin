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
    #여기는 html파일들 추가 해주세요.
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #여기 밑에는 CRUD 경로 입니다.
    path('creat/',views.creat,name='creat'),
    path('update/<int:item_id>',views.update,name='update'),
    path('creat/<int:item_id>',views.update,name='delete'),
]
