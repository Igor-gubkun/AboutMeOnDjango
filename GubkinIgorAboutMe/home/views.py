from django.shortcuts import render
from django.views.generic.base import TemplateView

class home(TemplateView):
    template_name = "GubkinIgorAboutMe/home.html"
