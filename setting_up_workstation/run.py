from setting_up_workstation.linux import ForLinux
from setting_up_workstation.windows import ForWidows
from sys import platform


def run():
    install = {
                'win32': ForWidows(),
                'linux': ForLinux()
            }
    run_setup = install.get(platform, 'Упс...\nЧто-то пошло не так...')
    run_setup.set_up()
