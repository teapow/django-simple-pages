from django_dynamic_fixture import G
from django.test import TestCase

from ..models import Page


class PageFallbackMiddlewareTestCase(TestCase):

    def test_process_response(self):
        """ Tests the process_response method of the middleware. """
        # Confirm that requests to 'valid' endpoints are processed properly.
        response = self.client.get('/admin/')
        self.assertNotEqual(response.status_code, 404)

        # Try to access a non-existant path.
        response = self.client.get(path='/test')
        self.assertEqual(response.status_code, 404)

        # Create a page with the same access_url.
        page = G(model=Page, access_url='/test', fill_nullable_fields=False)

        response = self.client.get(path='/test')
        self.assertEqual(response.status_code, 200)

        # Setup a redirect, and check the response.
        page.redirect_url = 'http://google.com'
        page.save()

        response = self.client.get(path='/test')
        self.assertEqual(response.status_code, 302)
