"""Celery inside django task manager."""
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import datetime


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketSpammer.settings')

app = Celery('socketSpammer')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.update(
    CELERYBEAT_SCHEDULE={
         'realtime-demo-every-1-seconds': {
            'task':
                'spammer.tasks.periodic_send_handler',
            'schedule': datetime.timedelta(seconds=1),
            'args': ()
        }
    }
)

