from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./habits.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    completions = relationship("HabitCompletion", back_populates="habit", cascade="all, delete-orphan")


class HabitCompletion(Base):
    __tablename__ = "habit_completions"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    completion_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    habit = relationship("Habit", back_populates="completions")


Index('idx_completion_date_habit', HabitCompletion.completion_date, HabitCompletion.habit_id)
Index('idx_habit_completion_date', HabitCompletion.habit_id, HabitCompletion.completion_date)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
