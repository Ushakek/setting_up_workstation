from setuptools import setup, find_packages
version = {}
# Загрузка версии из файла _version.py
with open('setting_up_workstation/_version.py', 'r') as version_file:
    exec(version_file.read(), version)


setup(
    name='setting-up-workstation',
    version=version['__version__'],
    author='npk_vip',
    description='Скрипт для настройки виртуального окружения на автоматизированном рабочем месте',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests == 2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'setting_up = setting_up_workstation.run:run',
        ],
    },
)
