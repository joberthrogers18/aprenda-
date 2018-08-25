from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import FormView
from .models import Course
from django.urls import reverse_lazy
from .forms import ContactCourse
from django.core.mail import send_mail
from django.conf import settings

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

class CourseDetailView(DetailView, FormView):
    model = Course
    template_name = 'courses/course_detail.html'
    form_class = ContactCourse
    success_url = reverse_lazy(
        viewname = 'courses:index',
    )

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['form'] = ContactCourse
        return context

    def send_mail(self):
        subject = 'Contato sobre Curso %s' % 'test'
        message  = 'Nome: %(name)s;Email: %(email)s;%(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL] )
    
