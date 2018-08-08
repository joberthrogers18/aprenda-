from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('contato/', views.ContactTemplateView.as_view(), name='contact')
]