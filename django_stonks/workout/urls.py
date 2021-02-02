from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='workout-home'),
    path('about/', views.about, name='workout-about')
]