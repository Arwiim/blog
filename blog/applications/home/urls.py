#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'registrer-suscription', 
        views.SubsxribersCreateView.as_view(),
        name='add-suscriptor',
    ),  
    path(
        'contact', 
        views.ConctactCreateView.as_view(),
        name='add-contact',
    ),  
]