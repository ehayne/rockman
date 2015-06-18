from __future__ import absolute_import, print_function
from gevent import monkey
monkey.patch_all()
from logan.runner import run_app


def main():
    run_app(
        project='rockman',
        default_config_path='~/.rockman/rockman.conf.py',
        default_settings='rockman.settings',
        settings_envvar='ROCKMAN_CONF',
    )


if __name__ == '__main__':
    main()
