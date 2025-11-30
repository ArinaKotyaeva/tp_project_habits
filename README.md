## Учёт привычек - CRUD-приложение для отслеживания ежедневных привычек

Демонстрация работы приложения: https://drive.google.com/file/d/1KQkc6udAI5AFX-GXJIFUWNM-KVoqFIpj/view?usp=sharing 

### Описание

Приложение позволяет пользователям:
- Создавать, редактировать и удалять привычки
- Отмечать привычки как выполненные за день
- Просматривать статистику выполнения за день и неделю
- Видеть процент выполнения привычек

## Технологии

### Backend
- **Python 3.11+**
- **FastAPI** 
- **SQLAlchemy** 
- **SQLite**

### Frontend
- **React 18** 
- **Vite** 
- **CSS3** 

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
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
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
- CI/CD с линтерами (flake8, pylint, eslint)

## Задачи каждого участника с описанием можно посмотреть тут:
https://miro.com/app/board/uXjVJioVWXs=/?share_link_id=356729867560
