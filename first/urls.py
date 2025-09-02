from django.urls import path
from . import views
from first import views as first_views

urlpatterns = [
    path("", views.home, name='home'),
]