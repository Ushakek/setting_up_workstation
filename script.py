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
        os.mkdir('temp')

    def download_an_install(self):
        if self.system == 'lin':
            url_python = 'https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz'
            name_py = './temp/Python.tgz'
            url_pc = 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.tar.gz?_gl=1*5yebku*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTEwOS4w&_ga=2.179933932.933493779.1621855103-287588693.1621344917'
            name_pc = './temp/PyCharm.tar.gz'
            url_sm = 'https://download.sublimetext.com/sublime-merge_build-2056_amd64.deb'
            name_sm = './temp/SublimeMerge.deb'
            url_git = 'https://mirrors.edge.kernel.org/pub/software/scm/git/git-manpages-2.9.5.tar.gz'
            name_git = './temp/GIT.tar.gz'

        elif self.system == 'win':
            url_python = 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe'
            name_py = r'..\temp\Python.exe'
            url_pc = 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917'
            name_pc = r'..\temp\PyCharm.exe'
            url_sm = 'https://download.sublimetext.com/sublime_merge_build_2056_x64_setup.exe'
            name_sm = r'..\temp\SublimeMerge.exe'
            url_git = 'https://github.com/git-for-windows/git/releases/download/v2.31.1.windows.1/Git-2.31.1-64-bit.exe'
            name_git = r'..\temp\GIT.exe'

        # download python3
        py = open(name_py, 'wb')
        download = requests.get(url_python)
        py.write(download.content)
        py.close()

        # download pycharm
        py_charm = open(name_pc, 'wb')
        download = requests.get(url_pc)
        py_charm.write(download.content)
        py_charm.close()

        # download sublime merge
        sublime_merge = open(name_sm, 'wb')
        download = requests.get(url_sm)
        sublime_merge.write(download.content)
        sublime_merge.close()

        # download git
        git = open(name_git, 'wb')
        download = requests.get(url_git)
        git.write(download.content)
        git.close()


my_system = Script()
print(my_system.system)
my_system.temp()
my_system.download_an_install()
