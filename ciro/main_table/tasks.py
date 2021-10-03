from asgiref.sync import async_to_sync

from django.forms.models import model_to_dict

from celery import shared_task
from channels.layers import get_channel_layer
import requests
from datetime import datetime

from .models import History


channel_layer = get_channel_layer()

@shared_task()
def get_post_info():
    url = 'http://127.0.0.1:8000/web/'
    data = requests.get(url).json()

    posts = []

    for info in data:
        obj, created = History.objects.get_or_create(caller=info['callerid'])

        obj.caller = info['callerid']
        obj.address = info['address']
        obj.name_object = info['name_object']
        obj.post_number = info['post_number']
        obj.status = info['status']
        obj.lastcall = datetime.fromtimestamp(int(info['lastcall'] or 0)).strftime('%H:%M')
        obj.category = info['category']

        if info['status'] == 'тревога':
            state = 'warning'
        elif info['status'] == 'норма':
            state = 'normal'
        elif info['status'] == None:
            state = 'normal'

        obj.save()

        new_data = model_to_dict(obj)
        new_data.update({'state': state})

        posts.append(new_data)

    async_to_sync(channel_layer.group_send)('main_table', {'type': 'send_new_data', 'text': posts})
