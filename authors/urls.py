from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.UserLogin.as_view(), name = 'login'),
    # path('login/', views.user_login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('update_profile/', views.update_profile, name = 'update_profile'),
    path('pass_change/', views.password_change, name = 'pass_change'),
    # path('logout/', views.user_logout, name = 'logout'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
]