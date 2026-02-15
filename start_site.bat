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
where %PYCMD% >nul 2>&1
if %errorlevel% neq 0 (
  echo Python not found. Use "Open portfolio (no server).bat" to view the site without a server.
  pause
  exit /b 1
)

echo Starting portfolio server in a new window...
echo Keep the "Portfolio Server" window OPEN. Closing it stops the site.
echo.
start "Portfolio Server" cmd /k "cd /d %ROOT% && echo. && echo Serving at http://127.0.0.1:8000/ && echo Site: http://127.0.0.1:8000/ && echo. && echo Keep this window open. Ctrl+C to stop. && echo. && %PYCMD% -m http.server 8000"
timeout /t 5 /nobreak >nul
start http://127.0.0.1:8000/
echo Browser opened. Leave the "Portfolio Server" window open.
timeout /t 2 /nobreak >nul
