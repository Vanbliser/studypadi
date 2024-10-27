import os
from celery import Celery


# You use .setdefault() of os.environ to assure that your Django project’s settings.py
# module is accessible through the "DJANGO_SETTINGS_MODULE" key.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studypadi.settings')

# Create the Celery application instance and provide the name of the
# main module <Django app that contains celery.py> as an argument.
app = Celery('studypadi')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# Define the Django settings file as the configuration file for Celery and provide a namespace, "CELERY".
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# Tell your Celery application instance to automatically find all tasks in each app of your Django project.
# This works as long as you stick to the structure of reusable apps and define all Celery tasks for an app in a dedicated tasks.py module.
app.autodiscover_tasks()
