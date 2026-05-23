from django.urls import path
from .views import *

urlpatterns =[
    path('',home,name='home'),
    path('cart/',cart,name='cart'),
    path('addcart/<int:pk>',addcart,name='addcart'),
    path('increase/<int:pk>',increase,name='increase'),
    path('decrease/<int:pk>',decrease,name='decrease'),
    path('delete_/<int:pk>',delete_,name='delete_')
]