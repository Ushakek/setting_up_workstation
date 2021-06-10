from setting_up_workstation.linux import ForLinux
from setting_up_workstation.windows import ForWidows
from sys import platform


def run():
    install = {
                'win32': ForWidows(),
                'linux': ForLinux()
            }

    if platform in install:
        install[platform].set_up()
    else:
        print('Упс...\nЧто-то пошло не так. Обратитесь к разработчику или администратору!')


if __name__ == '__main__':
    run()
