from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                CreateView, UpdateView, DeleteView)
from . import models


class IndexView(TemplateView):
    template = 'basic_app/index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name', 'principal')


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
