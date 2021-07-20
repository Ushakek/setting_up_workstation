from setting_up_workstation.base_script import Script
import os


class ForLinux(Script):
    """ Класс методов установки программ для Linux

    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """

    def sudo_check(self):
        """ Проверка пользователя

        Проверяет пользователя на знание пароля sudo, что бы не возникло ошибок при установке. Если пользователь вводит
        пароль неверно 3 раза, то выход из программы
        """

        result = os.system('sudo apt update')
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

        print('==== Начинаю установку! ====')
        self.try_install('sudo killall apt')
        self.try_install('sudo apt install python3')
        self.try_install('sudo apt-get install python3.9.*')
        self.try_install('sudo apt install snap')
        self.try_install('sudo apt install git')
        self.try_install('sudo snap install pycharm-community --classic')
        self.try_install('sudo killall apt')
        self.try_install('sudo apt update')
        print('==== Установка завершена ====')

    def requirements(self):
        """ Создание sh файла для установления зависимостей

            Создаёт sh файл, который устанавливает зависимости
        """

        os.system('python3.9 -m venv ./technological-process-smart-s-is/.venv ')
        with open('./technological-process-smart-s-is/update_requirements.sh', 'w', encoding='utf8') as file:
            file.write('.venv/bin/python3 -m pip install -r requirements.txt --force-reinstall')
        os.system('chmod u+x ./technological-process-smart-s-is/update_requirements.sh')

    def update_tp(self):
        """ Создание sh файла для обновления тех процесса

        Создаёт sh файл, который обновляет тех процесс
        """

        with open('./technological-process-smart-s-is/update_tp.sh', 'w', encoding='utf8') as file:
            file.write('git pull origin master develop')
        os.system('chmod u+x ./technological-process-smart-s-is/update_tp.sh')

    def run_tp(self):
        """ Создание sh файла по запуску тех процесса

        Создаёт sh файл, который устанавливает зависимости
        """

        with open('./technological-process-smart-s-is/run_tp.sh', 'w', encoding='utf8') as file:
            file.write('''source .venv/bin/activate
            export PYTHONPATH=$PYTHONPATH:./
            python3 ./smart_s_is/run.py''')
        os.system('chmod u+x ./technological-process-smart-s-is/run_tp.sh')

    def full_setup(self):
        """ Сценарий полной установки

        Сценарий полной установки. Включает в себя скачивание, установку, клонирование репозитория
        и добавление sh файлов
        """

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
        if not self.sudo_check():
            self.setup_choice(value)
            input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')