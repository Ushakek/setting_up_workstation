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
        """
        Метод для создания новой ветки с именем ARM'a от ветки develop. Ловим ошибку неправильного ввода пользователя.
        Вводиться должно только число.
        """
        os.chdir('technological-process-smart-s-is')
        os.system('git checkout develop')
        prefix_arm = 'ARM_'
        while True:
            number_of_arm = input('Введите номер ARM\nARM_')
            if not number_of_arm.isdigit():
                print('Пожалуйста, введите только число!')
            else:
                os.system(f'git checkout -b {prefix_arm + number_of_arm}')
                return False

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def set_up(self):
        pass
