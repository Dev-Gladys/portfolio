from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Project
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse, HttpResponse
from django.utils.html import strip_tags


def home(request):
    return HttpResponse("Welcome to my portfolio!")

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



@csrf_protect
def portfolio_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the sanitized data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # ... handle the form submission
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'}, status=400)
    return render(request, 'portfolio.html')
