from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, distinct
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
        week_start = today - timedelta(days=today.weekday())
    
    week_end = week_start + timedelta(days=6)
    
    total_habits = db.query(Habit).count()
    
    completed_habits_subquery = db.query(
        distinct(HabitCompletion.habit_id)
    ).filter(
        and_(
            HabitCompletion.completion_date >= week_start,
            HabitCompletion.completion_date <= week_end
        )
    ).subquery()
    
    completed_habits = db.query(completed_habits_subquery).count()
    
    completion_rate = (completed_habits / total_habits * 100) if total_habits > 0 else 0.0
    
    daily_stats = []
    current_date = week_start
    while current_date <= week_end:
        day_completed_count = db.query(HabitCompletion).filter(
            HabitCompletion.completion_date == current_date
        ).count()
        
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
