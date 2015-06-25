from __future__ import absolute_import, print_function
import os
from gevent import monkey
monkey.patch_all()
from logan.runner import run_app

ROOT = os.path.normpath(os.path.dirname(__file__))
CONF_FILEPATH = os.path.join(ROOT, "settings.py")


def main():
    run_app(
        project='rockman',
        default_config_path=CONF_FILEPATH,
        default_settings='rockman.settings',
    )


if __name__ == '__main__':
    main()
