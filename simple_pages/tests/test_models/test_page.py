from django_dynamic_fixture import G
from django.core.exceptions import ValidationError
from django.test import TestCase

from ...models import Page


class PageTestCase(TestCase):

    def setUp(self):
        self.page = G(
            model=Page,
            title="Test Page",
            access_url='/test',
            fill_nullable_fields=False
        )
        """:type page: simple_pages.models.Page"""

    def test_unicode(self):
        """ Tests the __unicode__ method. """
        expected = '/test'
        actual = self.page.__str__()
        self.assertIsInstance(actual, str)
        self.assertEqual(expected, actual)

        # Once a redirect_url is set, the format changes.
        self.page.redirect_url = '/redirect'

        expected = '/test -> /redirect'
        actual = self.page.__str__()
        self.assertIsInstance(actual, str)
        self.assertEqual(expected, actual)

    def test_is_redirect(self):
        """ Tests the Page.is_redirect property. """
        self.assertIsNone(self.page.redirect_url)
        self.assertFalse(self.page.is_redirect)

        # Set the redirect_url and retest.
        self.page.redirect_url = '/redirect'
        self.assertTrue(self.page.is_redirect)

    def test_get_absolute_url(self):
        """ Tests the Page.get_absolute_url method. """
        expected = '/test'
        actual = self.page.get_absolute_url()
        self.assertEqual(expected, actual)

        # Change the url, then retest.
        self.page.access_url = '/alternate'

        expected = '/alternate'
        actual = self.page.get_absolute_url()
        self.assertEqual(expected, actual)

    def test_clean_1(self):
        """ Tests the Page.clean() method. """
        self.page.clean()

        self.page.access_url = "test"
        with self.assertRaises(ValidationError):
            self.page.clean()

    def test_clean_2(self):
        """ Tests the Page.clean() method. """
        self.page.clean()

        self.page.template_name = "/test"
        with self.assertRaises(ValidationError):
            self.page.clean()
