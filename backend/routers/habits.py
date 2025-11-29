from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
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
    habits = db.query(Habit).all()
    
    result = []
    for habit in habits:
        completion = db.query(HabitCompletion).filter(
            and_(
                HabitCompletion.habit_id == habit.id,
                HabitCompletion.completion_date == today
            )
        ).first()
        
        result.append(HabitWithCompletion(
            id=habit.id,
            name=habit.name,
            description=habit.description,
            created_at=habit.created_at,
            is_completed_today=completion is not None
        ))
    
    return result


@router.get("/{habit_id}", response_model=HabitWithCompletion)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    today = date.today()
    habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    completion = db.query(HabitCompletion).filter(
        and_(
            HabitCompletion.habit_id == habit.id,
            HabitCompletion.completion_date == today
        )
    ).first()
    
    return HabitWithCompletion(
        id=habit.id,
        name=habit.name,
        description=habit.description,
        created_at=habit.created_at,
        is_completed_today=completion is not None
    )


@router.put("/{habit_id}", response_model=HabitModel)
def update_habit(habit_id: int, habit_update: HabitUpdate, db: Session = Depends(get_db)):
    db_habit = db.query(Habit).filter(Habit.id == habit_id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    if habit_update.name is not None:
        db_habit.name = habit_update.name
    if habit_update.description is not None:
        db_habit.description = habit_update.description
    
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
    db.refresh(completion)
    return {"message": "Habit completed successfully", "completion": completion}


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

