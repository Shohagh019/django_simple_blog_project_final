from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('update_profile/', views.update_profile, name = 'update_profile'),
    path('pass_change/', views.password_change, name = 'pass_change'),
    path('logout/', views.user_logout, name = 'logout'),
]