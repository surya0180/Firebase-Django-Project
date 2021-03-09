from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles', views.profiles, name='profiles'),
    path('saveData', views.saveData, name='saveData')
]
