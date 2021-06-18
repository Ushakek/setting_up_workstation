cd..
cd..
cd "%cd%\setting_up_workstation"
pyinstaller --onefile --name=set_up_windows run.py
copy ".\dist\set_up_windows.exe"  ".\"
rmdir /Q /S __pycache__
rmdir /Q /S build
rmdir /Q /S dist
del set_up_windows.spec
cd..
move ".\setting_up_workstation\set_up_windows.exe" ".\build_scripts\build_windows"
@pause