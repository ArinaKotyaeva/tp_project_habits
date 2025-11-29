from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from datetime import date, timedelta
from typing import Optional

from database import get_db, Habit, HabitCompletion
from models import StatisticsDay, StatisticsWeek

router = APIRouter()


@router.get("/day", response_model=StatisticsDay)
def get_day_statistics(
    target_date: Optional[date] = Query(None, alias="date"),
    db: Session = Depends(get_db)
):
    if target_date is None:
        target_date = date.today()
    
    total_habits = db.query(Habit).count()
    
    completed_habits = db.query(HabitCompletion).filter(
        HabitCompletion.completion_date == target_date
    ).count()
    
    completion_rate = (completed_habits / total_habits * 100) if total_habits > 0 else 0.0
    
    return StatisticsDay(
        date=target_date,
        total_habits=total_habits,
        completed_habits=completed_habits,
        completion_rate=round(completion_rate, 2)
    )


@router.get("/week", response_model=StatisticsWeek)
def get_week_statistics(
    week_start: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    if week_start is None:
        today = date.today()
        days_since_monday = today.weekday()
        week_start = today - timedelta(days=days_since_monday)
    
    week_end = week_start + timedelta(days=6)
    
    total_habits = db.query(Habit).count()
    
    completions = db.query(HabitCompletion).filter(
        and_(
            HabitCompletion.completion_date >= week_start,
            HabitCompletion.completion_date <= week_end
        )
    ).all()
    
    completed_habit_ids = set(completion.habit_id for completion in completions)
    completed_habits = len(completed_habit_ids)
    
    completion_rate = (completed_habits / total_habits * 100) if total_habits > 0 else 0.0
    
    daily_stats = []
    current_date = week_start
    while current_date <= week_end:
        day_completions = [c for c in completions if c.completion_date == current_date]
        day_completed_count = len(set(c.habit_id for c in day_completions))
        day_rate = (day_completed_count / total_habits * 100) if total_habits > 0 else 0.0
        
        daily_stats.append(StatisticsDay(
            date=current_date,
            total_habits=total_habits,
            completed_habits=day_completed_count,
            completion_rate=round(day_rate, 2)
        ))
        current_date += timedelta(days=1)
    
    return StatisticsWeek(
        week_start=week_start,
        week_end=week_end,
        total_habits=total_habits,
        completed_habits=completed_habits,
        completion_rate=round(completion_rate, 2),
        daily_stats=daily_stats
    )

