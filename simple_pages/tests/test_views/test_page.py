from django.http import Http404
from django.test import RequestFactory, TestCase, override_settings
from django.utils.safestring import SafeData
from django_dynamic_fixture import G

from ...models import Page
from ...views import PageView


class PageViewTestCase(TestCase):
    """ Tests the various methods in the PageView class. """

    @classmethod
    def setUpClass(cls):
        """ Sets the initial state for this test case. """
        super(PageViewTestCase, cls).setUpClass()

        cls.request_factory = RequestFactory()
        cls.page = G(model=Page, access_url='/abc', fill_nullable_fields=False)

    def setUp(self):
        self.page_view = PageView()

    def test_dispatch(self):
        """ Tests the PageView.dispatch() method. """
        request = self.request_factory.get(path='/abc')
        response = self.page_view.dispatch(request=request)
        self.assertEqual(response.status_code, 200)

    def test_dispatch_404(self):
        """ Tests the PageView.dispatch() method. """
        request = self.request_factory.get(path='/')
        with self.assertRaises(Http404):
            self.page_view.dispatch(request=request)

    def test_dispatch_no_leading_slash(self):
        """ Tests the PageView.dispatch() method. """
        request = self.request_factory.get(path='abc')
        response = self.page_view.dispatch(request=request)
        self.assertEqual(response.status_code, 200)

    def test_dispatch_trailing_slash(self):
        """ Tests the PageView.dispatch() method. """
        request = self.request_factory.get(path='abc/')
        response = self.page_view.dispatch(request=request)
        self.assertEqual(response.status_code, 200)

    @override_settings(APPEND_SLASH=True)
    def test_dispatch_trailing_slash_true(self):
        """ Tests the PageView.dispatch() method. """
        G(model=Page, access_url='/def/', fill_nullable_fields=False)
        request = self.request_factory.get(path='/def')
        response = self.page_view.dispatch(request=request)
        self.assertEqual(response.status_code, 200)

    @override_settings(APPEND_SLASH=False)
    def test_dispatch_trailing_slash_false(self):
        """ Tests the PageView.dispatch() method. """
        G(model=Page, access_url='/def/', fill_nullable_fields=False)
        request = self.request_factory.get(path='/def')
        with self.assertRaises(Http404):
            self.page_view.dispatch(request=request)

    def test_get_context_data(self):
        """ Tests the PageView.get_context_data() method. """
        self.page_view.page = self.page
        context = self.page_view.get_context_data()

        self.assertIn('page', context.keys())
        self.assertEqual(context['page'].id, self.page.id)
        self.assertIsInstance(context['page'].title, SafeData)
        self.assertIsInstance(context['page'].content, SafeData)
