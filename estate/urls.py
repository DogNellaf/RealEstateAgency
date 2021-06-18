from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/houses', views.houses, name='houses'),
    path('catalog/rent', views.rent, name='rent'),
    path('catalog/land', views.land, name='land'),
    path('catalog/apartments', views.apartments, name='apartments'),
    path('services', views.services, name='services'),
    path('jobopenings', views.jobopenings, name='jobopenings'),
]
