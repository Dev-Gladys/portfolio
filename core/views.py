from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Project
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse, HttpResponse
from django.utils.html import strip_tags
from .models import GladysOro

def home(request):
     return HttpResponse("Welcome to my portfolio!")  # This needs to change

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



def about_view(request):
    # Get the first profile or create one if it doesn't exist
    gladys, created = GladysOro.objects.get_or_create(
        pk=1,
        defaults={
            'name': 'Gladys Oro',
            'role': 'Software Developer',
            'location': 'United States',
            'email': 'your-email@domain.com'
        }
    )
    
    context = {
        'person': gladys,
        'journey': gladys.journey(),
        'expertise': gladys.expertise(),
        'education': gladys.education(),
        'interests': gladys.interests(),
        'certifications': gladys.certifications(),
        'current_project': gladys.get_current_project(),
        'motto': gladys.motto
    }
    return render(request, 'about.html', context)




# def project_view(request):
#     projects = [
#         {
#             'title': 'Project Title 1',
#             'description': 'Project description goes here',
#             'image': 'https://placehold.co/600x400/1a1a1a/ffffff?text=Project+1'
#         },
#         {
#             'title': 'Project Title 2',
#             'description': 'Project description goes here',
#             'image': 'https://placehold.co/600x400/1a1a1a/ffffff?text=Project+2'
#         },
#         {
#             'title': 'Project Title 3',
#             'description': 'Project description goes here',
#             'image': 'https://placehold.co/600x400/1a1a1a/ffffff?text=Project+3'
#         }
#     ]
#     return render(request, 'project.html', {'projects': projects})
