from abc import abstractmethod
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
        while result != 0 and count != 0:
            result = self.git_clone()
            count -= 1

        if result != 0:
            sys.exit('something problems')
        else:
            print('==== Копирование завершено! ====')

    def git_clone(self):
        # print('==== Начинаю копирование! ====')
        os.system('git config --global http.sslverify false')
        os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')
        # print('==== Копирование завершено! ====')

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
                continue
            else:
                arm_name = prefix_arm + number_of_arm
                os.system(f'git config --global user.name {arm_name}')
                os.system(f'git config --global user.email {arm_name}@zaovip.ru')
                os.system(f'git checkout -b {arm_name}')

                return False

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
