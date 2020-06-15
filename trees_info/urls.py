from django.urls import path
from trees.trees_info import views

urlpatterns = [
    path('info/all/', views.index_info, name='index_info'),
]