===================
django-simple-pages
===================

`django-simple-pages` allows you to store HTML documents in models, which can
be served automatically without the need for hard-coded URL patterns.

Example use cases include:

* Serving a static website.
* Handling redirects for relocated resources.
* Verifying site ownership for Google Search Console.


Quick-start
===========

1. Install: ``pip install django-simple-pages``.
2. Add: ``simple_pages`` to your ``INSTALLED_APPS``.
3. Add: ``simple_pages.middleware.PageFallbackMiddleware`` to your ``MIDDLEWARE_CLASSES``.
4. Run: ``python manage.py migrate simple_pages``.


Usage
=====

Simply navigate to your ``/admin`` and create a new ``Page`` object.


Changelog
=========

+----------------+-----------------------------------------------------------+
| Version        | Description                                               |
+================+===========================================================+
| 0.1.1          | Fixes incorrect help_text on Page.template_name.          |
+----------------+-----------------------------------------------------------+
| 0.1            | Initial version.                                          |
+----------------+-----------------------------------------------------------+
