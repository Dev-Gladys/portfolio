from django.urls import path
from core import views
from core.views import  PortfolioView 

urlpatterns = [
    path('', PortfolioView.as_view(), name='home'), 
    #path('about/', about_view, name='about'),
    #path('projects/', project_view, name='projects'),
]
