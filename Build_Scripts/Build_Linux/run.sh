pyinstaller --onefile set_up_workstation.py
cp ./dist/set_up_workstation ./
rm -r build 
rm -r dist
rm -r __pycache__
