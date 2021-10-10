
cd /d %~dp0


@For /F "tokens=1,2,3 delims=:,. " %%A in ('echo %time: =0%') do @(
Set Hour=%%A
Set Minute=%%B
Set Second=%%C
Set Tm=%%A%%B%%C
)

set current_path=%CD%

::echo %current_path%\ve\Scripts\activate

CALL %current_path%\ve\Scripts\activate.bat

echo Running script...
%current_path%\ve\Scripts\python -u %current_path%\main.py

CALL deactivate.bat

echo Done
