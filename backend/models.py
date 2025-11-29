from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Habit(HabitBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class HabitCompletionBase(BaseModel):
    habit_id: int
    completion_date: date


class HabitCompletionCreate(HabitCompletionBase):
    pass


class HabitCompletion(HabitCompletionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class HabitWithCompletion(Habit):
    is_completed_today: bool


class StatisticsDay(BaseModel):
    date: date
    total_habits: int
    completed_habits: int
    completion_rate: float


class StatisticsWeek(BaseModel):
    week_start: date
    week_end: date
    total_habits: int
    completed_habits: int
    completion_rate: float
    daily_stats: list[StatisticsDay]

