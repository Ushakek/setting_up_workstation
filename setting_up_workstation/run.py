from construct import Script
from linux import ForLinux
from windows import ForWidows
from sys import platform

if __name__ == '__main__':
    run = Script()
    if platform == 'win32':
        print(run.system)
        run_win = ForWidows()
        run_win.set_up()
    elif platform == 'linux':
        print(run.system)
        run_linux = ForLinux()
        run_linux.set_up()
    else:
        print(run.system)
