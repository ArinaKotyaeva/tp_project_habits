@echo off
echo ========================================
echo   Запуск Backend сервера
echo ========================================
echo.

cd backend

REM Проверка наличия виртуального окружения
if not exist "venv" (
    echo Создание виртуального окружения...
    python -m venv venv
)

REM Активация виртуального окружения
echo Активация виртуального окружения...
call venv\Scripts\activate

REM Установка зависимостей
echo Установка зависимостей...
pip install -r requirements.txt --quiet

REM Запуск сервера
echo.
echo ========================================
echo   Backend запущен на http://localhost:8000
echo   Нажмите Ctrl+C для остановки
echo ========================================
echo.
python run.py

pause

