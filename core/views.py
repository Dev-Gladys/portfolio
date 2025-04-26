from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.contrib import messages
from .models import Project
from .forms import ContactForm

class PortfolioView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
        else:
            messages.error(request, 'Error sending message. Please try again.')
        return self.get(request, *args, **kwargs)