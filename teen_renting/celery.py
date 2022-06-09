from __future__ import absolute_import, unicode_literals    # 保证 celery.py不和library冲突
import logging
import os
from celery import Celery
from celery.schedules import crontab

logger = logging.getLogger()

# 指定Django默认配置文件模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teen_renting.settings')
# 为项目创建一个Celery实例。这里不指定broker容易出现错误。
app = Celery('teen_renting', broker='redis://127.0.0.1:6379/4', backend='redis://127.0.0.1:6379/5')
# 这里指定从django的settings.py里读取celery配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动从所有已注册的django app中加载任务
app.autodiscover_tasks()


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