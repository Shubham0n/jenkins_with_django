from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company.settings")

app = Celery("company")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(["company.shared_task"])

app.conf.beat_schedule = {
    "update_student_course_object": {
        "task": "company.shared_task.add_data_every_minute",
        "schedule": crontab(minute="*"),
    }
}
