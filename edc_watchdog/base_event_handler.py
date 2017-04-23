import os
import pwd

from django.utils import timezone
from watchdog.events import PatternMatchingEventHandler


class BaseEventHandler(PatternMatchingEventHandler):
    """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
    """

    def __init__(self, hostname=None, remote_user=None, trusted_host=None, verbose=None):
        super().__init__(ignore_directories=True)
        self.hostname = hostname or 'localhost'
        self.remote_user = remote_user or pwd.getpwuid(os.getuid()).pw_name
        self.trusted_host = True if (
            trusted_host or self.hostname == 'localhost') else False
        self.verbose = True if verbose is None else verbose

    def process(self, event):
        self.output_to_console(
            '{} {} {} Not handled.'.format(timezone.now(), event.event_type, event.src_path))

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

    def on_deleted(self, event):
        self.process(event)

    def on_moved(self, event):
        self.process(event)

    def output_to_console(self, msg):
        if self.verbose:
            print(msg)
