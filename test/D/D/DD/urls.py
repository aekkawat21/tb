from django.urls import path

from DD import views


urlpatterns = [
    path('', views.home, ),
    path('edit/<int:id>/',  views.edit),
]