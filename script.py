from sys import platform
# import requests
import urllib.request


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

    def download_an_install(self):
        if self.system == 'lin':
            url_python = 'https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz'
            name_py = 'Python.tgz'
            url_PyCharm = 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.tar.gz?_gl=1*5yebku*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTEwOS4w&_ga=2.179933932.933493779.1621855103-287588693.1621344917'
            name_PC = 'PyCharm.tar.gz'

        elif self.system == 'win':
            url_python = 'https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe'
            name_py = 'Python.exe'
            url_PyCharm = 'http://download.jetbrains.com/python/pycharm-community-2021.1.1.exe?_gl=1*1vc7rdn*_ga*Mjg3NTg4NjkzLjE2MjEzNDQ5MTc.*_ga_V0XZL7QHEB*MTYyMTg1OTAzNi4zLjEuMTYyMTg1OTI4OC4w&_ga=2.209779037.933493779.1621855103-287588693.1621344917'
            name_PC = 'PyCharm.exe'


        download_Py = urllib.request.urlretrieve(url_python, name_py)
        download_PC = urllib.request.urlretrieve(url_PyCharm, name_PC)
    #    with open


my_system = Script()
print(my_system.system)
my_system.download_an_install()
