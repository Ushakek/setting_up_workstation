from setting_up_workstation.linux import ForLinux
from setting_up_workstation.windows import ForWidows
from sys import platform


def run():
    available_systems = {
                'win32': ForWidows(),
                'linux': ForLinux()
            }

    if platform in available_systems:
        available_systems[platform].set_up()
    else:
        print(f'Ваша платформа не поддерживается, ваша:\n {platform}\nДоступные: {available_systems.values()}')


if __name__ == '__main__':
    run()
