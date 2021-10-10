@echo off

cd /d %~dp0

@For /F "tokens=1,2,3 delims=:,. " %%A in ('echo %time: =0%') do @(
Set Hour=%%A
Set Minute=%%B
Set Second=%%C
Set Tm=%%A%%B%%C
)

if exist "ve\" (
  echo "virtualenvironment exists." 
) else (
  echo "Creating virtual environment..."
  python -m venv ve
)

if exist "ve\" (
    echo "installing packages...."
) else (
    echo "virtual environment does not exist" && EXIT -1
)

set current_path=%CD%

echo %current_path%\ve\Scripts\activate

CALL %current_path%\ve\Scripts\activate.bat

pip install -r requirements.txt

::CALL deactivate.bat

echo Done

pause
