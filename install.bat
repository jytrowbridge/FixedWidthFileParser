:: install packages:
pip install pywin32
pip install pyinstaller

:: Write current directory to config file:
@echo off
set "dir=%cd%"
set "dir=%dir:\=/%"
@echo ico_dir = "%dir%/lib/" >> lib\config.py

:: create exe:
pyinstaller.exe --windowed --"icon=%cd%\lib\jack.ico" ""%cd%\lib\parser.py"

:: create shortcuts:
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Start Menu\Programs\Fixed Width Parser.lnk');$s.TargetPath='%cd%\dist\parser\parser.exe';$s.Save()"
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Desktop\FW FILE PARSER.lnk');$s.TargetPath='%cd%\dist\parser\parser.exe';$s.Save()"
