from django.urls import path
from . import views, views
from rest_framework_simplejwt.views import TokenRefreshView

from .views import user_register, user_login, user_password_change, delete_user

app_name = 'UserManagement'
urlpatterns = [
    path('register/',user_register.as_view(),name=""),
    path('login/',user_login.as_view(),name="login"),
    path('ChangePassword/',user_password_change.as_view(),name="Change Password"),
    path('DeleteUser/',delete_user.as_view(),name="Delete User"),
    path('refresh/',TokenRefreshView.as_view(),name="token_refresh")
]