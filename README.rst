=============================
Django App Shell
=============================

.. image:: https://badge.fury.io/py/django-app-shell.svg
    :target: https://badge.fury.io/py/django-app-shell

.. image:: https://travis-ci.org/DebVortex/django-app-shell.svg?branch=master
    :target: https://travis-ci.org/DebVortex/django-app-shell

.. image:: https://codecov.io/gh/DebVortex/django-app-shell/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/DebVortex/django-app-shell

Inspired by the `Using Django with service workers`_ talk by `Adrian Holovaty`_
from the DjangoCon Europe 2016, django-app-shell aims to provide an easy to use
and configure way of utilizing the `app shell`_ architecture from google.



.. _`Using Django with service workers`: https://opbeat.com/community/posts/using-django-with-service-workers-by-adrian-holovaty/
.. _`Adrian Holovaty`: http://www.holovaty.com/
.. _`app shell`: https://developers.google.com/web/fundamentals/architecture/app-shell

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

* client side caching using service worker (TODO)
* easy push notification API (TODO)
* offline use of page/features using service worker (TODO)

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
