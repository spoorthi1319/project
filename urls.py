"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",register,name="register"),
    path("employee/",employee,name="employee"),
    path("calci/",calci,name="calci"),
    path("",index,name="index"),
    path("home/",home,name="home"),
    path("marks/",marks,name="marks"),
    path("salary/",salary,name="salary"),
    path("network/",network,name="network"),
    path("keer/",keer,name="keer"),
    path("drink/",drink,name="drink"),
    path("hello/",hello,name="hello"),
    path("aaa/",aaa,name="aaa"),
    path("a1/",a1,name="a1"),
]