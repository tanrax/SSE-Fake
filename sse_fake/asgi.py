# sse_fake/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
import django_eventstream
from django_eventstream import send_event
from faker import Faker
from random import randint
from time import sleep
import threading

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sse_fake.settings")

application = ProtocolTypeRouter(
    {
        # Django's ASGI application to handle traditional HTTP requests
        "http": URLRouter(
            [
                re_path(
                    r"^events/",
                    AuthMiddlewareStack(
                        URLRouter(django_eventstream.routing.urlpatterns)
                    ),
                    {"channels": ["events"]},
                ),
                re_path(r"", get_asgi_application()),
            ]
        ),
    }
)


def send_random_event():
    fake = Faker()
    while True:
        random_event = randint(0, 2)
        random_data = ""
        if random_event == 0:
            # User connected
            random_data = {"action": "User connected", "name": fake.first_name()}
        elif random_event == 1:
            # User disconnected
            random_data = {"action": "User disconnected", "name": fake.first_name()}
        elif random_event == 2:
            # New message
            random_data = {
                "action": "New message",
                "name": fake.first_name(),
                "text": fake.text(),
            }
        send_event(
            "events",
            "message"
            ,
            random_data,
        )
        sleep(randint(1, 5))

# Run in other thread send_random_event()
threading.Thread(target=send_random_event).start()