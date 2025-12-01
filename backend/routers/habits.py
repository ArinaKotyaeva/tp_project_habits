from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_, case
from datetime import date
from typing import List

from database import get_db, Habit, HabitCompletion
from models import HabitCreate, HabitUpdate, Habit as HabitModel, HabitWithCompletion

router = APIRouter()


@router.post("/", response_model=HabitModel)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    db_habit = Habit(name=habit.name, description=habit.description)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit


@router.get("/", response_model=List[HabitWithCompletion])
def get_habits(db: Session = Depends(get_db)):
    today = date.today()
    
    habits_with_completion = db.query(
        Habit,
        case(
            (db.query(HabitCompletion.id)
             .filter(
                 and_(
                     HabitCompletion.habit_id == Habit.id,
                     HabitCompletion.completion_date == today
                 )
             ).exists(), True),
            else_=False
        ).label('is_completed_today')
    ).all()
    
    return [
        HabitWithCompletion(
            id=habit.id,
            name=habit.name,
            description=habit.description,
            created_at=habit.created_at,
            is_completed_today=is_completed_today
        )
        for habit, is_completed_today in habits_with_completion
    ]


@router.get("/{habit_id}", response_model=HabitWithCompletion)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    today = date.today()
    
    habit_data = db.query(
        Habit,
        case(
            (db.query(HabitCompletion.id)
             .filter(
                 and_(
                     HabitCompletion.habit_id == Habit.id,
                     HabitCompletion.completion_date == today
                 )
             ).exists(), True),
            else_=False
        ).label('is_completed_today')
    ).filter(Habit.id == habit_id).first()
    
    if not habit_data:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    habit, is_completed_today = habit_data
    
    return HabitWithCompletion(
        id=habit.id,
        name=habit.name,
        description=habit.description,
        created_at=habit.created_at,
        is_completed_today=is_completed_today
    )


@router.put("/{habit_id}", response_model=HabitModel)
def update_habit(habit_id: int, habit_update: HabitUpdate, db: Session = Depends(get_db)):
    db_habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    update_data = habit_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_habit, field, value)
    
    db.commit()
    db.refresh(db_habit)
    return db_habit


@router.delete("/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    db_habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    db.delete(db_habit)
    db.commit()
    return {"message": "Habit deleted successfully"}


@router.post("/{habit_id}/complete")
def complete_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    today = date.today()
    
    existing = db.query(HabitCompletion).filter(
        and_(
            HabitCompletion.habit_id == habit_id,
            HabitCompletion.completion_date == today
        )
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Habit already completed today")
    
    completion = HabitCompletion(habit_id=habit_id, completion_date=today)
    db.add(completion)
    db.commit()
    return {"message": "Habit completed successfully"}


@router.delete("/{habit_id}/complete")
def uncomplete_habit(habit_id: int, db: Session = Depends(get_db)):
    today = date.today()
    completion = db.query(HabitCompletion).filter(
        and_(
            HabitCompletion.habit_id == habit_id,
            HabitCompletion.completion_date == today
        )
    ).first()
    
    if not completion:
        raise HTTPException(status_code=404, detail="Completion not found")
    
    db.delete(completion)
    db.commit()
    return {"message": "Habit uncompleted successfully"}
