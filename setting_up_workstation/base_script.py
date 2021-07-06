from abc import abstractmethod
from subprocess import Popen, PIPE
from sys import exit
import os


class Script:
    """ Класс базовых функций

    Этот клас содержит базовые методы работы скрипта, а так же описание обязательных методов у "Предков"

    """

    def print_system(self, user_system):
        """ Печать названия системы

        Печатает название системы пользователя
        Args:
            user_system: Наименование системы пользователя
        """

        print(f'==== Ваша система {user_system} ====')

    def check_git_authentication(self):
        """ Проверка авторизации git

        Проверяет пользовательскую авторизацию в git. Если в течении 3-х попыток у пользователя не удалось
        авторизоваться - прекращает выполнение программы
        """

        print('==== Начинаю копирование! ====')
        result = True
        count = 3
        while result is not False and count != 0:
            result = bool(self.git_clone())
            count -= 1
            continue

        if result is not False:
            exit('Не удалось авторизоваться!')
        else:
            print('==== Копирование завершено! ====')

    def git_clone(self):
        """ Клонирование репозитория git
        """
        os.system('git config --global http.sslverify false')
        system_code = os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')
        return system_code

    def create_name(self):
        """ Создание имени ветки

        Позволяет создать имя ветки или переключиться на существующую
        Returns:
            name: имя ветки новой/старой, если такая уже существовала
        """

        prefix_arm = 'ARM_'
        while True:
            number_of_arm = input('Введите номер ARM\nARM_')
            if not number_of_arm.isdigit():
                print('Пожалуйста, введите только число!')
                continue
            else:
                break

        name = prefix_arm + number_of_arm
        return name

    def check_name(self, full_name):
        """ Проверка имени ветки

        Позволяет создать имя ветки или переключиться на существующую. Проверяет имена всех локальных веток
        Args:
            full_name: Полное имя созданное методом create_name
        Returns:
            full_name: имя ветки новой/старой, если такая уже существовала
        """

        s = Popen('git branch', stdout=PIPE, shell=True, encoding='utf-8')
        branches = s.stdout.read()
        branches = branches.split('\n')

        for branch in branches:
            if branch.lower().lstrip() == full_name.lower():
                return branch
            elif branch.replace('_', '').lower().lstrip() == full_name.replace('_', '').lower():
                return branch
            else:
                continue

        return full_name

    def git_config(self):
        """ Конфигурация git

        Метод для создания новой ветки с именем ARM'a от ветки develop. Ловим ошибку неправильного ввода пользователя.
        Вводиться должно только число.
        Проверка, запускает методы проверки на ввод имени. Поиск совпадений имён
        """

        os.chdir('technological-process-smart-s-is')
        os.system('git checkout develop')
        arm_name = self.create_name()
        branch_name = self.check_name(arm_name)
        if arm_name == branch_name:
            os.system(f'git config --global user.name {arm_name}')
            os.system(f'git config --global user.email {arm_name}@zaovip.ru')
            os.system(f'git checkout -b {arm_name}')
        else:
            os.system(f'git config --global user.name {branch_name}')
            os.system(f'git config --global user.email {branch_name}@zaovip.ru')
            os.system(f'git checkout {branch_name}')
        os.chdir('..')

    def setup_menu(self):
        """ Меню установки
        Returns:
            set_up_script: Выбранный сценарий установки
        """

        set_up_script = input('''Выберите вариант установки:
            1) Полная установка
            2) Без установки программ(скопировать проект, добавить скрипты)
            3) Добавить только скрипты\nНапишите номер варианта(1, 2, 3): ''')

        while True:
            if not set_up_script.isdigit():
                set_up_script = input('Повторите ввод, только число от 1 до 3: ')
                continue
            elif int(set_up_script) not in range(1, 4):
                set_up_script = input('Повторите ввод, только число от 1 до 3: ')
                continue
            else:
                break

        set_up_script = int(set_up_script)
        return set_up_script

    @abstractmethod
    def install(self):
        pass

    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def requirements(self):
        pass

    @abstractmethod
    def update_tp(self):
        pass

    @abstractmethod
    def run_tp(self):
        pass