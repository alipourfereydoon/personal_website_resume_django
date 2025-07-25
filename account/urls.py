from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login',views.user_login, name='login-user'),
    path('logout',views.user_logout),
    path('register',views.user_register)
]
