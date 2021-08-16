from django.urls import path
from authentication import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

]