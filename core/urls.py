from django.urls import path
from .views import about_view
from core import views
from core.views import PortfolioView, about_view

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('about/', about_view, name='about'),
]
