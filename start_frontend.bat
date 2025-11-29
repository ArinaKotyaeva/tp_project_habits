@echo off
echo ========================================
echo   Запуск Frontend сервера
echo ========================================
echo.

cd frontend

REM Проверка наличия node_modules
if not exist "node_modules" (
    echo Установка зависимостей...
    npm install
)

REM Запуск dev сервера
echo.
echo ========================================
echo   Frontend запущен на http://localhost:3000
echo   Нажмите Ctrl+C для остановки
echo ========================================
echo.
npm run dev

pause

