from construct import Script
import os
import requests


class ForWidows(Script):
    """
    Сценарий установки для Windows, взаимодействие осуществляется через командную строку
    """
    def download(self):
        """
        Сценарий для скачивания программ. Пути и названия программ записаны как ключи в словаре, а ссылки на
        скачивание, как значения этих ключей. Запускаются циклом.
        Перед началом цикла создаётся "Временная папка, куда загружаются установочные образы
        """
        print('==== Начинаю скачивание! ====')
        try:
            os.mkdir('temp')
        except FileExistsError:  # ловим ошибку созданной папки
            print('Папка "temp" уже существует!')
            pass

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
        print('==== Скачивание завершено! ====')

    def state(self):
        """
        Данный метод создаёт временный файл, для продолжения установки с нужного нам момента(после перезапуска программы)
        """
        with open('.temp.txt', 'w', encoding='utf8') as file:
            file.write('git_key')

    def check_state(self):
        """
        Этот метод предназначен для чтения файла, после запуска программы. Так же он решает, что программа будет делать
        дальше
        """
        key = 'git_key'
        try:
            with open('.temp.txt', 'r') as file:
                if key in file:
                    return True
        except FileNotFoundError:
            return False

    def rm_state(self):
        """
        Этот метод нужен для удаления временного файла
        """
        try:
            os.system('del .temp.txt')
        except FileNotFoundError:
            pass

    def install(self):
        """
        Установка скачанных файлов.
        Перед циклом создаёт список с программами, которые нужно будет установить, потом перемещается в расположение
        скачанных файлов. Далее, используя цикл и автоподстановку запускается процесс установки программ, которые
        регулирует "настройщик"
        """

        print('==== Начинаю установку! ====')
        print('Пожалуйста, настройте устанавливаемые пакеты')
        print('НЕ ЗАБУДТЬЕ ПОСТАВИТЬ ГАЛОЧКУ ПРИ УСТАНОВКЕ PYTHON "ADD TO PATH" ')
        # перемешаемся в паку скачанных файлов
        programs = os.listdir('./temp')
        # запускаем установку
        os.chdir('./temp')
        for program in programs:
            os.system('{}'.format(program))
        os.chdir('../')
        print('=== Установка завершена! ===')

    # todo ИЗМЕНЁН ПРОЦЕСС ПРОВЕРКИ ДИРЕКТОРИИ, НЕ ТЕСТИЛ
    # todo ИЗМЕНЁН ПРОЦЕСС СКАЧИВАНИЯ, НЕ ТЕСТИЛ
    def check_dir(self):
        to_download = []
        urls = {'./temp/Python.exe': 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
                  './temp/PyCharm.exe': 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917',
                  './temp/SublimeMerge.exe': 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe',
                  './temp/GIT.exe': 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'}

        # проверим программы в папке temp
        programs = os.listdir('./temp')
        for program in urls.keys():
            if program in programs:
                print('{} was downloaded'.format(program))
            else:
                to_download.append('./temp/{}'.format(program)) # изменил процесс проверки. не тестил
        return to_download
    #     # создаём список скачанных файлов
    #     # В ПРОЦЕССЕ РАЗРАБОТКИ
    # Нужно попробовать запустить в отдельном файле проверку.

    def set_up(self):
        if not self.check_state():
            print(self.system)
            self.download()
            self.install()
            self.state()
            input('=== Установка не завершена, пожалуйста, перезапустите программу, что бы продолжить установку ===')
        else:
            self.git_clone()
            self.rm_state()
            input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')


start = ForWidows()
start.set_up()
