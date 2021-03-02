from django.urls import path
from django.urls.resolvers import URLPattern
from app import views

urlpatterns = [
    path('',views.index, name='index'),
    path('interestbased',views.interestbased, name='interestbased'),
    path('books',views.books, name='books'),
    path('biography',views.biography, name='Biography'),
    path('drama',views.drama, name='Drama'),
    path('fantasy',views.fantasy, name='Fantasy'),
    path('fiction',views.fiction, name='Fiction'),
    path('romance',views.romance, name='Romance'),
    path('scifi',views.scifi, name='Scifi'),
    path('thriller',views.thriller, name='Thriller'),
    path('cossim',views.cossim, name='cossim'),
    path('pearson',views.pearson, name='pearson'),


]