from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView , ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class LandingView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class BlogView(TemplateView):
    template_name = "blog.html"