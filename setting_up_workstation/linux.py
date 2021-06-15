from setting_up_workstation.base_script import Script
import os


class ForLinux(Script):
    """
    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """

    def sudo_check(self):
        result = os.system('sudo apt update')
        if result == 25600:
            return False
        else:
            print('Отмена установки.\nВведён неверный пароль!')
            return True

    def install(self):
        """
        Запускается установка через командную строку, требуется ввод пароля администратора
        В начале запускается обновление списка пакетов, в конце запускается обновление списка пакетов, а следом
        обновление этих пакетов.
        """
        print('==== Начинаю установку! ====')
        os.system('sudo killall apt')
        os.system('sudo apt install python3')
        os.system('sudo apt install virtualenv')
        os.system('sudo apt install snap')
        os.system('sudo apt install git')
        os.system('sudo snap install pycharm-community --classic')
        os.system('sudo killall apt')
        os.system('sudo apt update')
        print('==== Установка завершена ====')

    def requirements(self):
        os.system('virtualenv ./technological-process-smart-s-is/.venv ')
        with open('./technological-process-smart-s-is/update_requirements.sh', 'w', encoding='utf8') as file:
            file.write('.venv/bin/python3 -m pip install -r requirements.txt --force-reinstall')
        os.system('chmod u+x ./technological-process-smart-s-is/update_requirements.sh')

    def update_tp(self):
        with open('./technological-process-smart-s-is/update_tp.sh', 'w', encoding='utf8') as file:
            file.write('git pull origin master develop')
        os.system('chmod u+x ./technological-process-smart-s-is/update_tp.sh')

    def run_tp(self):
        with open('./technological-process-smart-s-is/run_tp.sh', 'w', encoding='utf8') as file:
            file.write('''source .venv/bin/activate
            export PYTHONPATH=$PYTHONPATH:./
            python3 ./smart_s_is/run.py''')
        os.system('chmod u+x ./technological-process-smart-s-is/run_tp.sh')

    def set_up(self):
        __system = 'Linux'
        self.print_system(__system)
        if not self.sudo_check():
            self.install()
            self.git_clone()
            self.name_arm()
            self.requirements()
            self.update_tp()
            self.run_tp()

            input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')
