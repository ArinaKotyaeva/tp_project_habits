# Учёт привычек

Веб-приложение для отслеживания ежедневных привычек с красивым интерфейсом и статистикой.

## Описание

Приложение позволяет пользователям:
- Создавать, редактировать и удалять привычки
- Отмечать привычки как выполненные за день
- Просматривать статистику выполнения за день и неделю
- Видеть процент выполнения привычек

## Технологии

### Backend
- **Python 3.11+**
- **FastAPI** - современный веб-фреймворк
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - база данных

### Frontend
- **React 18** - библиотека для создания пользовательского интерфейса
- **Vite** - инструмент сборки
- **CSS3** - стилизация с градиентами и анимациями

## Структура проекта

```
tp_project/
├── backend/                 # Backend приложение
│   ├── __init__.py
│   ├── main.py             # Точка входа FastAPI
│   ├── models.py           # Pydantic модели
│   ├── database.py         # Настройка БД и SQLAlchemy модели
│   ├── requirements.txt    # Python зависимости
│   ├── .flake8            # Конфигурация flake8
│   ├── .pylintrc          # Конфигурация pylint
│   └── routers/           # API роутеры
│       ├── __init__.py
│       ├── habits.py      # CRUD операции для привычек
│       └── statistics.py  # Статистика за день/неделю
│
├── frontend/               # Frontend приложение
│   ├── src/
│   │   ├── App.jsx        # Главный компонент
│   │   ├── App.css
│   │   ├── main.jsx       # Точка входа React
│   │   ├── index.css
│   │   └── components/    # React компоненты
│   │       ├── HabitsList.jsx
│   │       ├── HabitCard.jsx
│   │       ├── HabitForm.jsx
│   │       └── Statistics.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── .eslintrc.cjs
│
├── .github/
│   └── workflows/
│       └── ci.yml         # CI конфигурация
│
├── .gitignore
└── README.md
```

## Установка и запуск

### Требования
- Python 3.11+
- Node.js 18+
- npm или yarn

### Backend

1. Перейдите в директорию backend:
```bash
cd backend
```

2. Создайте виртуальное окружение (если еще не создано):
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Запустите сервер:
```bash
python run.py
```

База данных инициализируется автоматически при первом запуске приложения.

Backend будет доступен по адресу: http://localhost:8000

### Frontend

1. Перейдите в директорию frontend:
```bash
cd frontend
```

2. Установите зависимости (если еще не установлены):
```bash
npm install
```

3. Запустите dev-сервер:
```bash
npm run dev
```

Frontend будет доступен по адресу: http://localhost:3000

## API Endpoints

### Привычки

- `GET /api/habits/` - Получить все привычки
- `GET /api/habits/{id}` - Получить привычку по ID
- `POST /api/habits/` - Создать новую привычку
- `PUT /api/habits/{id}` - Обновить привычку
- `DELETE /api/habits/{id}` - Удалить привычку
- `POST /api/habits/{id}/complete` - Отметить привычку как выполненную сегодня
- `DELETE /api/habits/{id}/complete` - Снять отметку о выполнении

### Статистика

- `GET /api/statistics/day?date=YYYY-MM-DD` - Статистика за день
- `GET /api/statistics/week?week_start=YYYY-MM-DD` - Статистика за неделю

## Особенности

- Полный CRUD для привычек
- Отметка выполнения сохраняется на весь день
- Статистика за день и неделю с переключением
- Современный дизайн с градиентами
- Адаптивная верстка для мобильных устройств
- CI/CD с линтерами (flake8, pylint, eslint)

## Разработка

### Линтинг

**Backend:**
```bash
cd backend
flake8 .
pylint backend/
```

**Frontend:**
```bash
cd frontend
npm run lint
```

### Сборка

**Frontend:**
```bash
cd frontend
npm run build
```

