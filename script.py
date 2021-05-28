from sys import platform
import requests
import os


class Script(object):
    """
    Класс с конструктором. Родитель остальных классов
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

        try:
            os.mkdir('temp')
        except(FileExistsError):
            print('Temp does already exist')

        print('Start download!')

        urls = {'./temp/Python.exe': 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
                './temp/PyCharm.exe': 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917',
                './temp/SublimeMerge.exe': 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe',
                './temp/GIT.exe': 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'}

        # Скачиваем файлы
        for path in urls.keys():
            program = open(path, 'wb')
            download = requests.get(urls[path])
            program.write(download.content)
            program.close()

    def install(self):
        print('Now we install!')
        # перемешаемся в паку скачанных файлов
        programs = os.listdir('./temp')
        # запускаем установку
        os.chdir('./temp')
        for program in programs:
            os.system('{}'.format(program))

    # def check_dir(self):
    #       to_download = []
    #     # проверим программы в папке temp
    #     programs = os.listdir('./temp')
    #     for program in urls:
    #         if program in programs:
    #             print('{} was downloaded'.format(program))
    #         else:
    #             programs_to_download.append(program)
    #
    #     # скачаем то, что ещё не скачано
    #     # для каждого из пути
    #     for path in urls.keys():
    #         # для каждого из НЕ скачанного
    #         for i in to_download:
    #             # если путь в "НЕ скачанном", то скачиваем
    #             if path == i:
    #                 program = open(path, 'wb')
    #                 download = requests.get(urls[path])
    #                 program.write(download.content)
    #                 program.close()
    #     # создаём список скачанных файлов
    #     # В ПРОЦЕССЕ РАЗРАБОТКИ


class ForLinux(Script):
    """
    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """
    def install(self):
        os.system('sudo apt install python3')
        os.system('sudo apt install snap')
        os.system('sudo apt install git')
        os.system('sudo snap install pycharm-community --classic')


def work_with_git():
    # Функция общего сценария для обоих систем
    print('yeah! we do this!')
    os.system('git config --global http.sslverify false')
    os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')


def process_of_install():
    this_system = Script()
    print(this_system.system)
    if this_system.system == 'Your system is Windows':
        win = ForWidows()
        win.download()
        win.install()
        work_with_git()
    elif this_system.system == 'Your system is Linux':
        lin = ForLinux()
        lin.install()
        work_with_git()


process_of_install()

