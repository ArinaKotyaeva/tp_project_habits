@echo off
echo ========================================
echo   Запуск всего проекта
echo ========================================
echo.

REM Запуск Backend в новом окне
echo Запуск Backend сервера...
start "Backend Server" cmd /k "cd backend && python -m venv venv && call venv\Scripts\activate && pip install -r requirements.txt --quiet && python run.py"

REM Небольшая задержка
timeout /t 3 /nobreak >nul

REM Запуск Frontend в новом окне
echo Запуск Frontend сервера...
start "Frontend Server" cmd /k "cd frontend && if not exist node_modules (npm install) && npm run dev"

echo.
echo ========================================
echo   Оба сервера запущены!
echo   Backend:  http://localhost:8000
echo   Frontend: http://localhost:3000
echo ========================================
echo.
echo Откройте браузер и перейдите на http://localhost:3000
echo.
pause

