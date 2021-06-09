pyinstaller --onefile set_up_workstation.py
copy ".\dist\set_up_workstation.exe"  ".\"
rmdir /Q /S __pycache__
rmdir /Q /S build
rmdir /Q /S dist
@pause