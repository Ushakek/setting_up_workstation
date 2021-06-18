cd ..
cd ..
BASEDIR=$(dirname $(realpath "$0"))
cd $BASEDIR/setting_up_workstation
pyinstaller --onefile --name=set_up_linux run.py
cp ./dist/set_up_linux $BASEDIR/build_scripts/build_linux
rm -r build 
rm -r dist
rm -r __pycache__
rm set_up_linux.spec

