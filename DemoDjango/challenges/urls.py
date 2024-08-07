from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>/', views.number_month_challenge, name="number_mouth_challenge"),
    path('<str:month>/', views.month_challenge, name='mouth_challenge'),
]