from sys import platform
import requests
import os


class Script(object):
    """
    Пока что не до конца понимаю зачем тут класс, но вроде так делают умные люди
    """
    def __init__(self):
        # linux
        if platform == 'linux':
            self.system = 'lin'

        # windows
        elif platform == 'win32':
            self.system = 'win'

    def temp(self):
        try:
            os.mkdir('temp')
        except(FileExistsError):
            print('Temp does already exist')

    def download_and_install_win(self):
        programs_to_download = []

        urls = {'./temp/Python.exe': 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe',
                './temp/PyCharm.exe': 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917',
                './temp/SublimeMerge.exe': 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe',
                './temp/GIT.exe': 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'}

        # проверим программы в папке temp
        programs = os.listdir('./temp')
        for program in urls:
            if program in programs:
                print('{} was downloaded'.format(program))
            else:
                programs_to_download.append(program)


        for prog in urls:
            for i in programs_to_download:
                if prog == i:
                    program = open(prog, 'wb')
                    download = requests.get(urls[prog])
                    program.write(download.content)
                    program.close()

        programs = os.listdir('./temp')
        os.chdir('./temp')

        for i in programs:
            os.system('{}'.format(i))

    def install_lin(self):
        os.system('sudo apt install python3')
        os.system('sudo apt install snap')
        os.system('sudo apt install git')
        os.system('sudo snap install pycharm-community --classic')
        os.system('git clone https://gitlab-srv.corp.npkvip.ru/technological-processes/technological-process-smart-s-is')


my_system = Script()
print(my_system.system)
my_system.temp()
if my_system.system == 'win':
    my_system.download_and_install_win()
elif my_system.system == 'lin':
    my_system.install_lin()
