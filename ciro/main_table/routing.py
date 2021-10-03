from django.urls import path

from .consumers import CoinsConsumer

ws_urlpatterns = [
    path('ws/main_table/', CoinsConsumer.as_asgi())
]