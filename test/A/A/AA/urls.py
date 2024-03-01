from django.urls import path
from AA import views


urlpatterns = [
    path('', views.home),
]