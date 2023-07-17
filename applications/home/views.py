import datetime

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .models import Breakfast, Lunch, Dinner


class HomePageView(TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy("authentication_app:auth-login")


class BreakfastCreateView(CreateView):
    model = Breakfast
    template_name = "home/create-breakfast.html"
