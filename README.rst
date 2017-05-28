=============================
Django App Shell
=============================

.. image:: https://badge.fury.io/py/django-app-shell.svg
    :target: https://badge.fury.io/py/django-app-shell

.. image:: https://travis-ci.org/DebVortex/django-app-shell.svg?branch=master
    :target: https://travis-ci.org/DebVortex/django-app-shell

.. image:: https://codecov.io/gh/DebVortex/django-app-shell/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/DebVortex/django-app-shell

Easy use service workers and the app shell concept for django.

Documentation
-------------

The full documentation is at https://django-app-shell.readthedocs.io.

Quickstart
----------

Install Django App Shell::

    pip install django-app-shell

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_app_shell.apps.DjangoAppShellConfig',
        ...
    )

Add Django App Shell's URL patterns:

.. code-block:: python

    from django_app_shell import urls as django_app_shell_urls


    urlpatterns = [
        ...
        url(r'^', include(django_app_shell_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
