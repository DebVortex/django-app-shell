=====
Usage
=====

To use Django App Shell in a project, add it to your `INSTALLED_APPS`:

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
