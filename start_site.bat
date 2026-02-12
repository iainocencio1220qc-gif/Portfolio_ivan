@echo off
set "ROOT=%~dp0"
set "LOGFILE=%ROOT%_batch_ran.txt"
echo batch_started %date% %time%>>"%LOGFILE%"
cd /d "%ROOT%"

where py >nul 2>&1
if %errorlevel% equ 0 (
  set PYCMD=py
) else (
  set PYCMD=python
)

echo Starting portfolio server...
start "Portfolio Server" cmd /k "cd /d %ROOT%static && echo. && echo Serving at http://127.0.0.1:8000/ && echo Keep this window open. Press Ctrl+C to stop. && echo. && %PYCMD% -m http.server 8000"
timeout /t 3 /nobreak >nul
start http://127.0.0.1:8000/
echo Browser opened. Close this window; server runs in the other window.
timeout /t 2 /nobreak >nul
