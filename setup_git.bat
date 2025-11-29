@echo off
echo ========================================
echo   Настройка Git для проекта
echo ========================================
echo.

REM Переходим в директорию проекта
cd /d "%~dp0"

REM Удаляем lock файл из домашней папки (если есть)
echo Удаление lock файла...
del "C:\Users\Арина Котяева\.git\index.lock" 2>nul

REM Инициализируем git в правильной директории
echo Инициализация Git репозитория...
git init

REM Добавляем remote
echo Добавление remote...
git remote remove origin 2>nul
git remote add origin https://github.com/ArinaKotyaeva/tp_project_habits.git

REM Добавляем файлы
echo Добавление файлов...
git add .

REM Показываем статус
echo.
echo ========================================
echo   Статус Git:
echo ========================================
git status

echo.
echo ========================================
echo   Следующие шаги:
echo ========================================
echo 1. Проверьте, что в статусе только файлы проекта
echo 2. Выполните: git commit -m "Initial commit"
echo 3. Выполните: git push -u origin main
echo.
pause

