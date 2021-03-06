from setting_up_workstation.base_script import Script
import os


class ForLinux(Script):
    """ Класс методов установки программ для Linux

    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """

    command_list = [
        'sudo apt-get install snap',
    ]

    def update_install(self):
        self.install_list()
        for program in self._list_programs:
            if program == 'Python':
                self.command_list.append('sudo apt-get install python 3.9.*')
            elif program == 'PyCharm':
                self.command_list.append('sudo snap install pycharm-community --classic')
            elif program == 'GIT':
                self.command_list.append('sudo apt-get install git')
            elif program == 'Sublime-merge':
                self.command_list.append('snap install sublime-merge --classic')


    def sudo_check(self):
        """ Проверка пользователя

        Проверяет пользователя на знание пароля sudo, что бы не возникло ошибок при установке. Если пользователь вводит
        пароль неверно 3 раза, то выход из программы
        """
        os.system('killall apt')
        result = os.system('sudo apt update')
        os.system('killall apt')
        os.system('killall unattended-upgr')
        if bool(result) is False:
            return False
        else:
            print('Отмена установки.\nВведён неверный пароль!')
            return True

    def try_install(self, command):
        """ Запуск команд в оболочке системы

        Запускает поочерёдно команды оболочки
        Args:
            command: команда оболочки
        """

        try:
            os.system(command)
        except Exception as e:
            print(e)

    def install(self):
        """ Сценарий установки

        Запускается установка через командную строку, требуется ввод пароля администратора
        В начале запускается обновление списка пакетов, в конце запускается обновление списка пакетов, а следом
        обновление этих пакетов.
        """

        self.update_install()

        print('==== Начинаю установку! ====')
        for command in self.command_list:
            self.try_install(command)
        print('==== Установка завершена ====')

    def requirements(self):
        """ Создание sh файла для установления зависимостей

            Создаёт sh файл, который устанавливает зависимости
        """

        os.system(f'python3.9 -m venv ./{self._path_to_script}/.venv ')
        with open(f'./{self._path_to_script}/update_requirements.sh', 'w', encoding='utf8') as file:
            file.write('.venv/bin/python3 -m pip install -r requirements.txt --force-reinstall')
        os.system(f'chmod u+x ./{self._path_to_script}/update_requirements.sh')

    def update_tp(self):
        """ Создание sh файла для обновления тех процесса

        Создаёт sh файл, который обновляет тех процесс
        """

        with open(f'./{self._path_to_script}/update_tp.sh', 'w', encoding='utf8') as file:
            file.write('git pull origin master develop')
        os.system(f'chmod u+x ./{self._path_to_script}/update_tp.sh')

    def run_tp(self):
        """ Создание sh файла по запуску тех процесса

        Создаёт sh файл, который устанавливает зависимости
        """

        with open(f'./{self._path_to_script}/run_tp.sh', 'w', encoding='utf8') as file:
            file.write(f'''source .venv/bin/activate
            export PYTHONPATH=$PYTHONPATH:./
            python3 {self.find_run()}/run.py''')
        os.system(f'chmod u+x ./{self._path_to_script}/run_tp.sh')

    def full_setup(self):
        """ Сценарий полной установки

        Сценарий полной установки. Включает в себя скачивание, установку, клонирование репозитория
        и добавление sh файлов
        """

        if not self.sudo_check():
            self.install()
            self.check_git_authentication()
            self.git_config()
            self.requirements()
            self.update_tp()
            self.run_tp()

    def base_setup(self):
        """ Создание sh файла по запуску тех процесса

        Создаёт sh файл, который устанавливает зависимости
        """

        self.check_git_authentication()
        self.git_config()
        self.requirements()
        self.update_tp()
        self.run_tp()

    def minimal_setup(self):
        """ Сценарий минимальной установки

        Этот сценарий включает в себя только лишь добавление sh файлов в репозиторий
        """
        self.choice_project()
        self.requirements()
        self.update_tp()
        self.run_tp()

    def setup_choice(self, temp):
        """ Определение выбора установки

        Опираясь на выбор пользователя переходит к сценарию выполнения
        Args:
            temp: Номер выбранной пользователем установки
        """

        if temp == 1:
            self.full_setup()
        elif temp == 2:
            self.base_setup()
        elif temp == 3:
            self.minimal_setup()

    def set_up(self):
        """ Сценарий запуска программы

        Запускает программу, даёт пользователю выбор желаемой установки
        """

        value = self.setup_menu()
        __system = 'Linux'
        self.print_system(__system)
        self.setup_choice(value)
        input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')