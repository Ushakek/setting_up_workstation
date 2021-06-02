from construct import Script
import os
import requests
import subprocess


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
        print('start download')
        # try:
        #     os.mkdir('temp')
        # except FileExistsError:  # ловим ошибку созданной папки
        #     print('Temp does already exist')
        #     pass
        #
        # print('Start download!')
        #
        # urls = {'./temp/Python.exe': 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
        #         './temp/PyCharm.exe': 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917',
        #         './temp/SublimeMerge.exe': 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe',
        #         './temp/GIT.exe': 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'}
        #
        # # program = open('./temp/GIT.exe', 'wb')
        # # download = requests.get(urls['./temp/GIT.exe'])
        # # program.write(download.content)
        # # program.close()
        # # выше лишние 4 строки
        #
        # # Скачиваем файлы
        # for path in urls.keys():
        #     program = open(path, 'wb')
        #     download = requests.get(urls[path])
        #     program.write(download.content)
        #     program.close()
        print('finished download')

    def reboot(self):
        # перезагрузка командной строки методом запуска новой
        print('Command of reboot cmd')
        # obj_git = Script()
        # try:
        #     # Работает только в powershell нужно попробовать "'powershell {}'.format()" и запустить
        #     subprocess.Popen('{}'.format(obj_git.git_clone()), creationflags=subprocess.DETACHED_PROCESS)
        # except FileNotFoundError:
        #     pass
        print('Cmd has been rebooted')

    def install(self):
        """
        Установка скачанных файлов.
        Перед циклом создаёт список с программами, которые нужно будет установить, потом перемещется в расположение
        скачанных файлов. Далее, используя цикл и автоподстановку запускается процесс установки программ, которые
        регулирует "настройщик"
        """

        print('Start install!')
        # # перемешаемся в паку скачанных файлов
        # programs = os.listdir('./temp')
        # # запускаем установку
        # os.chdir('./temp')
        # # os.system('GIT.exe')
        # for program in programs:
        #     os.system('{}'.format(program))
        # os.chdir('../')
        print('Finished install')

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
