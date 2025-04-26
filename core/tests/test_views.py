import pytest
from django.urls import reverse
from core.models import Project

@pytest.mark.django_db
class TestPortfolioView:
    def test_portfolio_view_get(self, client):
        response = client.get(reverse('portfolio'))
        assert response.status_code == 200
        
    def test_contact_form_submission(self, client):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        response = client.post(reverse('portfolio'), data)
        assert response.status_code == 200