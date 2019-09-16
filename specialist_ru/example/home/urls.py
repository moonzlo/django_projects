from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('logn/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout_user'),
    

]