from django.urls import path
from .views import *
urlpatterns=[
    path('register/',register,name='register'),
    path('login_',login_,name='login_'),
    path('profile/',profile_,name='profile_'),
    path('forgot/',forget,name='forget_'),
    path('logout_/',logout_,name='logout_'),
    path('reset/',reset_pasw,name='reset_pasw'),
    path('update/',update,name='update'),
]