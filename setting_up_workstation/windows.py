from setting_up_workstation.base_script import Script
import os
import requests


class ForWidows(Script):
    """
    Сценарий установки для Windows, взаимодействие осуществляется через командную строку
    """

    def check_dir(self, urls):
        """
        Метод для проверки уже скачанных программ
        Нужен на случай, если установка пошла не так, что бы не скачивать всё по второму разу.
        Возвращает список программ, которые находятся в папке temp (папка должна находиться в корне вместе с программой)
        """
        to_download = []

        # проверим программы в папке temp
        programs = os.listdir('./temp')
        for program in urls.keys():
            if program.replace('./temp/', '') in programs:
                print(f'{program} уже был скачан!')
            else:
                to_download.append(f'{program}')
        return to_download

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
        need_download = self.check_dir(urls)
        for path in need_download:
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
        os.system('attrib +h ".temp.txt"')

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
            os.system('attrib -h ".temp.txt"')
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

    def requirements(self):
        os.system('python -m venv ./technological-process-smart-s-is/.venv')
        with open(r'.\technological-process-smart-s-is\update_requirements.bat', 'w', encoding='utf8') as file:
            file.write('.venv\Scripts\python.exe -m pip install -r requirements.txt --force-reinstall\n@pause')

    def update_tp(self):
        with open(r'.\technological-process-smart-s-is\update_tp.bat', 'w', encoding='utf8') as file:
            file.write('git pull origin master develop\n@pause')

    def run_tp(self):
        with open(r'.\technological-process-smart-s-is\run_tp.bat', 'w', encoding='utf8') as file:
            file.write(r'''setlocal
            set PYTHONPATH=%cd%
            .venv\Scripts\python.exe smart_s_is\run.py
            endlocal
            @pause''')

    def full_setup(self):
        if not self.check_state():
            __system = 'Windows'
            self.print_system(__system)
            self.download()
            self.install()
            self.state()
            input('=== Установка не завершена, пожалуйста, перезапустите программу, что бы продолжить установку ===')
        else:
            self.check_git_authentication()
            self.rm_state()
            self.git_config()
            self.requirements()
            self.update_tp()
            self.run_tp()
            input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')

    def base_setup(self):
        self.check_git_authentication()
        self.git_config()
        self.requirements()
        self.update_tp()
        self.run_tp()
        input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')

    def minimal_setup(self):
        self.requirements()
        self.update_tp()
        self.run_tp()
        input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')

    def setup_choice(self, temp):
        if temp == 1:
            self.full_setup()
        elif temp == 2:
            self.base_setup()
        elif temp == 3:
            self.minimal_setup()

    def set_up(self):
        if not self.check_state():
            value = self.setup_menu()
            self.setup_choice(value)
        else:
            self.full_setup()