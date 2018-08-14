from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='index'),
    path('novo/', views.CourseCreateView.as_view(), name='create_course'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='detail_course'),
    #path('contato/', views.ContactTemplateView.as_view(), name='contact')
]