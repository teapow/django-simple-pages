- Add `django-simple-history==1.9.0` to your requirements.txt file.
- Add `'pages'` to your `INSTALLED_APPS`.
- Add `'simple_history'` to your `INSTALLED_APPS`.
- Add `'pages.middleware.PageFallbackMiddleware'` to your `MIDDLEWARE_CLASSES`.
- Run `python manage.py makemigrations pages`.
- Run `python manage.py migrate` to create the database tables.

To run tests, you'll need to ensure you have `django-dynamic-fixtures` installed.