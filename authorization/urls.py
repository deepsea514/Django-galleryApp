from django.urls import path,include
from .views import *



urlpatterns = [

  path('login', login, name='login'),
  path('register', register, name = 'register'),
  path('logout', logout, name='logout')
]
