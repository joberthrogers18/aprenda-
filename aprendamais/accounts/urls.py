'''
from django.urls import path
from . import views
from django.contrib.auth import login, logout

app_name = 'accounts'

urlpatterns = [
    path('entrar', login , {'template_name' : 'accounts/login.html'}, name='login'),
]
'''
