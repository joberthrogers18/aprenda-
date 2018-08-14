from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
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
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    success_url = reverse_lazy(
        viewname = 'courses:index',
    )

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    
