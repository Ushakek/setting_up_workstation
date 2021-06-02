from sys import platform
import requests
import os
import subprocess


class Script(object):
    """
    Класс с конструктором. Родитель остальных классов. В нём находится определитель системы.
    """
    def __init__(self):
        # linux
        if platform == 'linux':
            self.system = 'Your system is Linux'

        # windows
        elif platform == 'win32':
            self.system = 'Your system is Windows'


class ForWidows(Script):
    """
    Сценарий установки для Windows, взаимодействие осуществляется через командную строку
    """
    def download(self):
        """
        Сценарий для скачивания программ. Пути и названия программ записаны как ключи в словаре, а ссылки на
        скачивание, как значения этих ключей. Запускаются циклом.
        Перед началом цикла создаётся "Временная папка, куда загружаются устоновочные образы
        """

        try:
            os.mkdir('temp')
        except FileExistsError:  # ловим ошибку созданной папки
            print('Temp does already exist')
            pass

        print('Start download!')

        urls = {'./temp/Python.exe': 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
                './temp/PyCharm.exe': 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917',
                './temp/SublimeMerge.exe': 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe',
                './temp/GIT.exe': 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'}

        # program = open('./temp/GIT.exe', 'wb')
        # download = requests.get(urls['./temp/GIT.exe'])
        # program.write(download.content)
        # program.close()
        # выше лишние 4 строки

        # Скачиваем файлы
        for path in urls.keys():
            program = open(path, 'wb')
            download = requests.get(urls[path])
            program.write(download.content)
            program.close()

    def reboot(self):
        # перезагрузка командной строки методом запуска новой
        print('Command of reboot cmd')
        try:
            # Работает только в powershell нужно попробовать "'powershell {}'.format()" и запустить
            subprocess.Popen('{}'.format(work_with_git()), creationflags=subprocess.DETACHED_PROCESS)
        except FileNotFoundError:
            pass

    def install(self):
        """
        Установка скачанных файлов.
        Перед циклом создаёт список с программами, которые нужно будет установить, потом перемещется в расположение
        скачанных файлов. Далее, используя цикл и автоподстановку запускается процесс установки программ, которые
        регулирует "настройщик"
        """

        print('Start install!')
        # перемешаемся в паку скачанных файлов
        programs = os.listdir('./temp')
        # запускаем установку
        os.chdir('./temp')
        # os.system('GIT.exe')
        for program in programs:
            os.system('{}'.format(program))
        os.chdir('../')

    # ИЗМЕНЁН ПРОЦЕСС ПРОВЕРКИ ДИРЕКТОРИИ, НЕ ТЕСТИЛ
    # ИЗМЕНЁН ПРОЦЕСС СКАЧИВАНИЯ, НЕ ТЕСТИЛ
    # def check_dir(self):
    #       to_download = []
    #     # проверим программы в папке temp
    #     programs = os.listdir('./temp')
    #     for program in urls.keys():
    #         if program in programs:
    #             print('{} was downloaded'.format(program))
    #         else:
    #             to_download.append('./temp/{}'.format(program)) # изменил процесс проверки. не тестил
    #
    #     # скачаем то, что ещё не скачано
    #     # для каждого из пути
    #     # for path in urls.keys():
    #         # для каждого из НЕ скачанного
    #     for path in to_download:
    #         program = open(path, 'wb')
    #         download = requests.get(urls[path])
    #         program.write(download.content)
    #         program.close()
    #     # создаём список скачанных файлов
    #     # В ПРОЦЕССЕ РАЗРАБОТКИ
    # Нужно попробовать запустить в отдельном файле проверку.


class ForLinux(Script):
    """
    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """
    def install(self):
        """
        Запускается установка через командную строку, требуется ввод пароля администратора
        В начале запускается обновление списка пакетов, в конце запускается обновление списка пакетов, а следом
        обновление этих пакетов.
        """
        os.system('sudo apt update')
        os.system('sudo apt install python3')
        os.system('sudo apt install snap')
        os.system('sudo apt install git')
        os.system('sudo snap install pycharm-community --classic')
        os.system('sudo apt update')
        os.system('sudo apt upgrade')


def work_with_git():
    # Функция общего сценария для обоих систем по "склониванию" репозитория
    print('yeah! we do this!')
    os.system('git config --global http.sslverify false')
    os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')


def process_of_install():
    """
    Эта функция регулирует процесс установки программ
    """
    this_system = Script()
    print(this_system.system)
    if this_system.system == 'Your system is Windows':
        win = ForWidows()
        win.download()
        win.install()
        win.reboot()

    elif this_system.system == 'Your system is Linux':
        lin = ForLinux()
        lin.install()
        work_with_git()


process_of_install()
end = input('Installation finished\nPress enter to exit\n')
