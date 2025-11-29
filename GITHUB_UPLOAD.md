# 📤 Как загрузить проект на GitHub

## Шаг 1: Убедитесь, что вы в корне проекта

```bash
cd C:\Users\Арина Котяева\Desktop\MISIS\tp_project
```

## Шаг 2: Проверьте статус git

```bash
git status
```

## Шаг 3: Добавьте все файлы проекта

```bash
# Добавить все файлы (кроме тех, что в .gitignore)
git add .

# Или добавьте файлы по отдельности:
git add backend/
git add frontend/
git add .github/
git add *.md
git add *.bat
git add *.txt
git add .gitignore
```

## Шаг 4: Проверьте, что будет загружено

```bash
git status
```

Убедитесь, что НЕ добавляются:
- ❌ venv/ или ven/ (виртуальные окружения)
- ❌ node_modules/ (зависимости Node.js)
- ❌ *.db (базы данных)
- ❌ __pycache__/ (кэш Python)
- ❌ .vite/ (кэш Vite)

## Шаг 5: Сделайте commit

```bash
git commit -m "Initial commit: Habits Tracker application with FastAPI backend and React frontend"
```

## Шаг 6: Загрузите на GitHub

```bash
git push -u origin main
```

---

## ✅ Если всё прошло успешно

Откройте ваш репозиторий на GitHub:
https://github.com/ArinaKotyaeva/tp_project_habits

Вы должны увидеть все файлы проекта!

---

## 🔧 Если возникли проблемы

### Ошибка: "remote origin already exists"
```bash
# Удалите старый remote
git remote remove origin

# Добавьте заново
git remote add origin https://github.com/ArinaKotyaeva/tp_project_habits.git
```

### Ошибка: "failed to push some refs"
```bash
# Сначала получите изменения с GitHub
git pull origin main --allow-unrelated-histories

# Затем загрузите
git push -u origin main
```

### Если случайно добавили лишние файлы
```bash
# Удалите из индекса (но оставьте локально)
git rm --cached -r venv/
git rm --cached -r node_modules/
git rm --cached backend/habits.db

# Обновите .gitignore если нужно
# Затем снова commit
git commit -m "Remove ignored files"
git push
```

---

## 📝 Что должно быть в репозитории

✅ **Должно быть:**
- backend/ (код Python, но без venv/)
- frontend/ (код React, но без node_modules/)
- .github/workflows/ (CI конфигурация)
- README.md, ЗАПУСК.md и другие .md файлы
- .gitignore
- *.bat файлы для запуска
- requirements.txt, package.json

❌ **НЕ должно быть:**
- venv/, ven/ (виртуальные окружения)
- node_modules/ (зависимости)
- *.db (базы данных)
- __pycache__/ (кэш)
- .vite/ (кэш Vite)

