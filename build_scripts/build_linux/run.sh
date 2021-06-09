cd ..
cd ..
BASEDIR=$(dirname $(realpath "$0"))
echo $BASEDIR
cp $BASEDIR/setting_up_workstation/linux.py $BASEDIR/build_scripts/build_linux
cp $BASEDIR/setting_up_workstation/construct.py $BASEDIR/build_scripts/build_linux
cd build_scripts/build_linux
pyinstaller --onefile --name=set_up_linux linux.py
cp ./dist/set_up_linux ./
rm -r build 
rm -r dist
rm -r __pycache__
rm set_up_linux.spec
rm linux.py
rm construct.py
