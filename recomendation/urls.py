"""recomendation URL Configuration

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
from django.urls import  path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('books',views.books, name='books'),
    path('Biography',views.Biography, name='Biography'),
    path('Drama',views.Drama, name='Drama'),
    path('Fantasy',views.Fantasy, name='Fantasy'),
    path('Fiction',views.Fiction, name='Fiction'),
    path('Romance',views.Romance, name='Romance'),
    path('Sci-fi',views.Scifi, name='Scifi'),
    path('Thriller',views.Thriller, name='Thriller'),
    path('cossim',views.cossim, name='Thriller'),
    path('SVD',views.svd, name='Thriller'),
    
]
