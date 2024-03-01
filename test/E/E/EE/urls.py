from django.urls import path
from EE import views


urlpatterns = [
    path('', views.home, ),
    path('delete/<int:id>/',  views.delete),
]