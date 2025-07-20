@echo off

if not exist "venv\Scripts\activate.bat" goto ask_create

goto continue

:ask_create
set /p createVenv=Virtual environment not found. Create it now? (Y/N): 
if /I "%createVenv%"=="Y" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt >nul 2>&1
) else (
    echo Exiting.
    exit /b
)

:continue

echo [1] Starting WebSocket server...
start cmd /k "call venv\Scripts\activate.bat && python server.py"

timeout /t 2 >nul

echo [2] Starting scanner bridge...
start cmd /k "call venv\Scripts\activate.bat && python bridge.py"

timeout /t 2 >nul

echo [3] Starting HTTP server...
start cmd /k "call venv\Scripts\activate.bat && python -m http.server 8888"

timeout /t 2 >nul

echo [4] Opening browser...
start http://localhost:8888/index.html

echo [✓] All components started.
pause
