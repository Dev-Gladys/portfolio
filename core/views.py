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

          # about‑profile
        gladys, created = GladysOro.objects.get_or_create(
            pk=1,
            defaults={
                'name': 'Gladys Oro',
                'role': 'Software Developer',
                'location': 'United Kingdom',
                'email': 'ziglad.dev@gmail.com'
            }
        )
        context.update({
            'person':          gladys,
            'journey':         gladys.experience(),
            'expertise':       gladys.skills(),
            'education':       gladys.education(),
            'interests':       gladys.interests(),
            'certifications':  gladys.certifications(),
            #'current_project': gladys.get_current_project(),
            'motto':           gladys.motto,
        })

        return context


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Add a success message
            messages.success(request, 'Message sent successfully!')
            # Redirect to the same page to prevent duplicate submissions
            return redirect('home')
        else:
            # Add an error message
            messages.error(request, 'Error sending message. Please try again.')
            # Re-render the page with the form and error messages
            context = self.get_context_data(**kwargs)
            context['form'] = form  # Pass the form with errors back to the template
            return self.render_to_response(context)



