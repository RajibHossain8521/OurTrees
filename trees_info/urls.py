from django.urls import path
from . import views

urlpatterns = [
    path('info/all/', views.index_info, name='index_info'),
    #path('search/by/trees/<str:tree_name>', views.search_by_trees_name, name='search_by_trees_name'),
    #path('search/by/writer/<str:writername>', views.search_by_user_id, name='search_by_writer_name'),
]
