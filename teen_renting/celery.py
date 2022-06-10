from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, platforms
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teen_renting.settings')
app = Celery('base_django_api')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

platforms.C_FORCE_ROOT = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


'''
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'auto_update_paid': {
            'task': 'order.tasks.auto_update_paid',
            'schedule': crontab(minute=0, hour=0),    # 每天凌晨0点执行一次更新paid
            'args': (),
        },
        'send_email': {
            'task': 'order.tasks.send_email',
            'schedule': crontab(minute=0, hour=0),    # 每天中午11点05分执行一次群发消息
            'args': (),
        }
    }
)
'''