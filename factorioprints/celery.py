import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factorioprints.settings')
app = Celery('factorioprints')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
'send-reminder': {
    'task': 'printparser.tasks.auto_update_prints',
    'schedule': crontab()
  },
}