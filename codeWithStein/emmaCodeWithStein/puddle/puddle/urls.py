"""
URL configuration for puddle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include

# codeWithStein used this to import the index object 
# from core.views import  contact

urlpatterns = [
    path('', include('core.urls')),
    # path('contact/', contact, name="contact"), This to view contact
    # path('', index, name="index"), This to view index
    path('admin/', admin.site.urls),
]
