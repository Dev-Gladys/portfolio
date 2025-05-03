from django.urls import path
from .views import about_view
from core import views
from core.views import  about_view, project_view, PortfolioView

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'), 
    path('about/', about_view, name='about'),
    path('projects/', project_view, name='projects'),
]
