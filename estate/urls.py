from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('catalog/homes', views.homes, name='homes'),
    path('services', views.services, name='services'),
    path('jobopenings', views.jobopenings, name='jobopenings'),
]
