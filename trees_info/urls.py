from django.urls import path
from . import views

urlpatterns = [
    path('info/all/', views.index_info, name='index_info'),
]