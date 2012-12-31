from django.core.management.base import NoArgsCommand
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import zmq

class Command(NoArgsCommand):
    def handle_noargs(self, *args, **kwargs):
        pass