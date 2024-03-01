from django.urls import path

from CC import views


urlpatterns = [
    path('', views.home, ),
    path('search_name/', views.search_name ),
]