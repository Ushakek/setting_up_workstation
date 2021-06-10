from construct import Script
import os


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
        print('==== Начинаю установку! ====')
        os.system('sudo apt update')
        os.system('sudo apt install python3')
        os.system('sudo apt install snap')
        os.system('sudo apt install git')
        os.system('sudo snap install pycharm-community --classic')
        os.system('sudo apt update')
        os.system('sudo apt upgrade')
        print('==== Установка завершена ====')

    def set_up(self):
        print(self.system)
        self.install()
        self.git_clone()
        self.name_arm()
        input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')
