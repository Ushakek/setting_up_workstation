from setting_up_workstation.base_script import Script
import os


class ForLinux(Script):
    """
    Сценарий установки для Linux, взаимодействие осуществляется через командную строку
    """

    def sudo_check(self):
        result = os.system('sudo apt update')
        if bool(result) is False:
            return False
        else:
            print('Отмена установки.\nВведён неверный пароль!')
            return True

    def try_install(self, command):
        try:
            os.system(command)
        except Exception as e:
            print(e)

    def install(self):
        """
        Запускается установка через командную строку, требуется ввод пароля администратора
        В начале запускается обновление списка пакетов, в конце запускается обновление списка пакетов, а следом
        обновление этих пакетов.
        """
        print('==== Начинаю установку! ====')
        self.try_install('sudo killall apt')
        self.try_install('sudo apt install python3')
        self.try_install('sudo apt install virtualenv')
        self.try_install('sudo apt install snap')
        self.try_install('sudo apt install git')
        self.try_install('sudo snap install pycharm-community --classic')
        self.try_install('sudo killall apt')
        self.try_install('sudo apt update')
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

    def full_setup(self):
        self.install()
        self.check_git_authentication()
        self.git_config()
        self.requirements()
        self.update_tp()
        self.run_tp()

    def base_setup(self):
        self.check_git_authentication()
        self.git_config()
        self.requirements()
        self.update_tp()
        self.run_tp()

    def minimal_setup(self):
        self.requirements()
        self.update_tp()
        self.run_tp()

    def setup_choice(self, temp):
        if temp == 1:
            self.full_setup()
        elif temp == 2:
            self.base_setup()
        elif temp == 3:
            self.minimal_setup()

    def set_up(self):
        value = self.setup_menu()
        __system = 'Linux'
        self.print_system(__system)
        if not self.sudo_check():
            self.setup_choice(value)
            input('Установка полностью закончена\nНажмите "ENTER" что бы выйти')
