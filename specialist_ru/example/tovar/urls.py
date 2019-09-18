from django.urls import path
from . import views

app_name = 'tovar'
urlpatterns = [
    path('', views.price_list, name='price_list'),

    path('<int:id>/', views.show, name='show'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/add_picture/', views.add_picture, name='add_picture'),
    path('<int:id>/picture/', views.picture, name='picture'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/add_tags/', views.add_tags, name='add_tags'),
    path('<int:id>/<str:pk_tag>/drop/', views.drop_tag, name='drop_tag'),

    path('tags/', views.tag_list, name='tags_list'),
    path('group/', views.group_list, name='group_list'),
    path('create/', views.create, name='create'),
     path('graph/', views.graph, name='graph'),
    
    
]