from sys import platform
from abc import abstractmethod
import os


class Script(object):
    """
    Класс с конструктором. Родитель остальных классов. В нём находится определитель системы.
    """
    def __init__(self):

        system = {
            'win32': 'Windows',
            'linux': 'Linux'
        }

        self.system = '==== Ваша система {} ===='.format(system.get(platform, '"Неизвестная система"'))

    def git_clone(self):
        print('==== Начинаю копирование! ====')
        os.system('git config --global http.sslverify false')
        os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')
        print('==== Копирование завершено! ====')

    def name_arm(self):
        os.chdir('technological-process-smart-s-is')
        os.system('git checkout develop')
        arm = 'ARM_'
        while True:
            name = input('Введите номер ARM\nARM_')
            if not name.isdigit():
                print('Пожалуйста, введите только число!')
            else:
                os.system(f'git checkout -b {arm + name}')
                return False

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def set_up(self):
        pass
