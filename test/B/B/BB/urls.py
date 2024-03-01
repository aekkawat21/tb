from django.urls import path
from BB import views


urlpatterns = [
    path('', views.home, ),
    path('search_id/', views.search_id ),
]