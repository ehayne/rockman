from __future__ import absolute_import, print_function

import sys
import os

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option


class Command(BaseCommand):
    args = '<service>'
    help = 'Starts the specified service (default: http)'

    option_list = BaseCommand.option_list + (
        make_option('--debug',
            action='store_true',
            dest='debug',
            default=False),
        make_option('--workers', '-w',
            dest='workers',
            type=int,
            default=None),
        make_option('--noinput',
            action='store_true',
            dest='noinput',
            default=False,
            help='Tells Django to NOT prompt the user for input of any kind.',
        ),
    )

    def handle(self, service_name='http', address=None, **options):
        from rockman.services.http import HTTPServer

        loglevel = os.environ.get("LOGLEVEL", "info")
        if address:
            if ':' in address:
                host, port = address.split(':', 1)
                port = int(port)
            else:
                host = address
                port = None
        else:
            host, port = None, None

        services = {
            'http': HTTPServer,
        }

        try:
            service_class = services[service_name]
        except KeyError:
            raise CommandError('%r is not a valid service' % service_name)

        service = service_class(
            debug=options.get('debug'),
            host=host,
            port=port,
            workers=options.get('workers'),
            loglevel=loglevel,
        )

        # remove command line arguments to avoid optparse failures with service code
        # that calls call_command which reparses the command line
        sys.argv = sys.argv[:1]

        print("Running service: %r" % service_name)
        service.run()
