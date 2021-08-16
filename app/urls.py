from django.urls import path
from app import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('users/', views.users, name='users'),
    path('new_debate/', views.new_debate, name='new_debate'),
    path('debates/', views.debates, name='debates'),
    path('discussion/<str:pk>/', views.discussion, name='discussion'),


    path('jsonupdates/', views.jsonupdates, name='jsonupdates'),
]