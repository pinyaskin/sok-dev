import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ciro.settings')

app = Celery('ciro')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_30s': {
        'task': 'main_table.tasks.get_post_info',
        'schedule': 5.0
    }
}

app.autodiscover_tasks()

# celery -A ciro beat -l INFO
# celery -A ciro worker -l INFO