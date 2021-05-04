from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('trainer', views.trainer, name="trainer"),
    path('membership', views.membership, name="membership"),
    path('terms', views.terms, name="terms"),
    path('location', views.location, name="location")

]
