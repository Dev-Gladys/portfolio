import pytest
from django.urls import reverse
from django.core.exceptions import ValidationError
from core.models import Project
from django.utils.html import escape
import re

@pytest.mark.django_db
class TestPortfolioView:
    def test_portfolio_view_get(self, client):
        response = client.get(reverse('portfolio'))
        assert response.status_code == 200
        # Verify CSRF token is present in the response
        assert 'csrfmiddlewaretoken' in str(response.content)

    def test_contact_form_submission_with_csrf(self, client):
        # First get the page to retrieve the CSRF token
        response = client.get(reverse('portfolio'))
        assert response.status_code == 200

        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        # The client will automatically handle CSRF
        response = client.post(reverse('portfolio'), data)
        assert response.status_code == 200

    def test_contact_form_submission_without_csrf(self, client):
        # Disable CSRF verification for this client
        client.handler.enforce_csrf_checks = True
        
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        response = client.post(reverse('portfolio'), data)
        # Should fail with 403 Forbidden
        assert response.status_code == 403

    def test_form_validation(self, client):
        # Test invalid email
        data = {
            'name': 'Test User',
            'email': 'invalid-email',
            'message': 'Test message'
        }
        response = client.post(reverse('portfolio'), data)
        assert response.status_code == 400  # or whatever status code you return for invalid input

        # Test empty required fields
        data = {
            'name': '',
            'email': '',
            'message': ''
        }
        response = client.post(reverse('portfolio'), data)
        assert response.status_code == 400

    def test_input_sanitization(self, client):
        # Test XSS attempt
        malicious_input = '<script>alert("xss")</script>'
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': malicious_input
        }
        response = client.post(reverse('portfolio'), data)
        assert response.status_code == 200
        # Verify the script tags are escaped in the response
        assert '<script>' not in str(response.content)
        assert escape(malicious_input) in str(response.content)

    def test_email_validation(self, client):
        def is_valid_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return bool(re.match(pattern, email))

        test_emails = [
            ('test@example.com', True),
            ('invalid-email', False),
            ('test@.com', False),
            ('test@domain', False),
            ('@domain.com', False)
        ]

        for email, should_be_valid in test_emails:
            data = {
                'name': 'Test User',
                'email': email,
                'message': 'Test message'
            }
            response = client.post(reverse('portfolio'), data)
            expected_status = 200 if should_be_valid else 400
            assert response.status_code == expected_status