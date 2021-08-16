from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import course

# Create your views here.

class NewCourseView(CreateView):
    model = course
    fields = '__all__'

class ListCourseView(ListView):
    model = course
    context_object_name = 'courses'

class UpdateCourseView(UpdateView):
    model = course
    fields = '__all__'

class DeleteCourseView(DeleteView):
    model = course
    success_url = "/course/view"

