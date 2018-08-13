from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import Course
from django.urls import reverse_lazy

class CourseListView(ListView):
    model = Course
    template_name = 'courses/index.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/create_course.html'
    fields = [
        'name',
        'description',
        'image',
    ]

    success_url = reverse_lazy(
        viewname = 'courses:index',
    )
