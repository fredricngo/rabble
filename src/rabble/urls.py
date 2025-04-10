from django.urls import path
#urls.py will map URL patterns to view functions 
#determines what content the user sees when a URL path is visited 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile")
]

#when we request comes for the root, call views.index 