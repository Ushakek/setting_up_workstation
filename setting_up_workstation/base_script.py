from abc import abstractmethod
from subprocess import Popen, PIPE
import os
import sys


class Script:
    """
    Класс с конструктором. Родитель остальных классов. В нём находится определитель системы.
    """

    def print_system(self, user_system):
        print(f'==== Ваша система {user_system} ====')

    def check_git_authentication(self):
        print('==== Начинаю копирование! ====')
        result = 1
        count = 3
        while result > 0 and count != 0:
            result = self.git_clone()
            count -= 1

        if result != 0:
            sys.exit('something problems')
        else:
            print('==== Копирование завершено! ====')

    def git_clone(self):
        # print('==== Начинаю копирование! ====')
        os.system('git config --global http.sslverify false')
        system_code = os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')
        # print('==== Копирование завершено! ====')
        return system_code

    def create_name(self):
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
        """
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
