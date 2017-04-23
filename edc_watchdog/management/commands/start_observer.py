# -*- coding: utf-8 -*-

"""
    For example ...

"""

import socket
import sys

from builtins import ConnectionResetError, ConnectionRefusedError
from django.core.management.base import BaseCommand, CommandError
from paramiko import SSHException

from ...server import Server


def some_even_handler():
    pass


class Command(BaseCommand):

    help = ''

    def handle(self, *args, **options):

        event_handler = some_even_handler()

        try:
            server = Server(event_handler)
        except (ConnectionResetError, SSHException, ConnectionRefusedError, socket.gaierror) as e:
            raise CommandError(str(e))
        sys.stdout.write('\n' + str(server) + '\n')
        sys.stdout.write('\npress CTRL-C to stop.\n\n')
        server.observe()
