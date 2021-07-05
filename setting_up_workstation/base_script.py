from abc import abstractmethod
from subprocess import Popen, PIPE
from sys import exit
import os
import requests


class Script:
    """ Класс базовых функций

    Этот клас содержит базовые методы работы скрипта, а так же описание обязательных методов у "Предков"

    """
    _dict_prj = {}
    _path_to_script = ''
    _path_to_run = ''

    def print_system(self, user_system):
        """ Печать названия системы

        Печатает название системы пользователя
        Args:
            user_system: Наименование системы пользователя
        """

        print(f'==== Ваша система {user_system} ====')

    def check_directory(self):
        """Метод для проверки директории на наличие проекта

        Returns:
            булевый аргумент для обработки
        """

        for root, dirs, files in os.walk('./'):
            if self._path_to_script in dirs:
                return True

    def choice_project(self):
        self.get_projects()
        url = self.get_url_project(self._dict_prj)
        if self.check_directory():
            return None
        else:
            return url

    def check_git_authentication(self):
        """ Проверка авторизации git

        Проверяет пользовательскую авторизацию в git. Если в течении 3-х попыток у пользователя не удалось
        авторизоваться - прекращает выполнение программы
        """
        url = self.choice_project()
        # if not url:
        #     return None

        print('==== Начинаю копирование! ====')
        result = True
        count = 3
        while result is not False and count != 0:
            result = bool(self.git_clone(url))
            count -= 1
            continue

        if result is not False:
            input('Не удалось авторизоваться!\n Нажмите Enter, что бы выйти.')
            exit()
        else:
            print('==== Копирование завершено! ====')

    def get_projects(self):
        """Метод для поучения списка проектов

        Отправляет запрос на gitlab api, получает значения в виде словаря, который преобразует в словарь с "полезными данными"

        Returns:
            status_code: возвращает код выполнения
            Обновляет словарь
            _dict_prj: пара в виде:
                                   индекс: {
                                   'id': id проекта
                                   'name': имя проекта на русском
                                   'url': ссылка на доступ к проекту
                                   'path': наименование проекта на ангилийском
                                   }
        """
        _params = {'access_token': 'rgTD5jAxQycgx2XkNtef'}
        try:
            full_page = requests.get('https://gitlab-srv.corp.npkvip.ru/api/v4/groups/88/projects',
                                     verify=False, params=_params)

            if not full_page.status_code == 200:
                return full_page.status_code, full_page.text

            projects = full_page.json()
            for count, project in enumerate(projects, 1):
                self._dict_prj.update({
                    str(count): {
                        'id': project['id'],
                        'name': project['description'],
                        'url': project['web_url'],
                        'path': project['path'],
                    }
                })
            return full_page.status_code

        except Exception as Err:
            return Err, print(f'Что-то пошло не так: {Err}')

    def get_url_project(self, projects):
        """Метод для выбора проекта

        Показывает пользователю, какие проекты сейчас доступны для клонирования и даёт выбор по индексу
        Returns:
            projects[index_project]['url']: url проекта, по которому его можно склонировать
        """
        for project in projects:
            print(f'{project}: {projects[project]["name"]}')
        while True:
            index_project = input('Выберите проект: ')
            if not index_project.isdigit() or index_project not in projects.keys():
                print('Введите только индекс проекта!')
                continue
            else:
                self._path_to_script = projects[index_project]['path']
                break
        return projects[index_project]['url']

    def git_clone(self, url):
        """ Клонирование репозитория git
        """
        os.system('git config --global http.sslverify false')
        system_code = os.system(f'git clone {url}')
        return system_code

    def find_run(self):
        """Метод для поиска пути к стартовому файлу

        Returns:
             self._path_to_run: обновлённый путь до "бегущего" скрипта
        Problems:
            Возвращает первое вхождение => если есть установленные библиотеки, то может в них найти run.py и вернуть
            путь до него.
        """

        for root, dirs, files in os.walk(f'./{self._path_to_script}'):
            try:
                dirs.remove('.venv')
            except ValueError:
                pass
            if 'run.py' in files:
                self._path_to_run = os.path.join(root).replace(f'./{self._path_to_script}\\', '')
                self._path_to_run = os.path.join(root).replace(f'./{self._path_to_script}/', '')
                return self._path_to_run

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

        os.chdir(f'{self._path_to_script}')
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

    @abstractmethod
    def full_setup(self):
        pass

    @abstractmethod
    def base_setup(self):
        pass

    @abstractmethod
    def minimal_setup(self):
        pass
