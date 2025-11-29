import React from 'react'
import './HabitCard.css'

function HabitCard({ habit, onEdit, onDelete, onToggleComplete }) {
  return (
    <div className={`habit-card ${habit.is_completed_today ? 'completed' : ''}`}>
      <div className="habit-header">
        <h3>{habit.name}</h3>
        <div className="habit-actions">
          <button
            className="btn-icon"
            onClick={() => onEdit(habit)}
            title="Редактировать"
          >
            ✏️
          </button>
          <button
            className="btn-icon"
            onClick={() => onDelete(habit.id)}
            title="Удалить"
          >
            🗑️
          </button>
        </div>
      </div>
      
      {habit.description && (
        <p className="habit-description">{habit.description}</p>
      )}
      
      <div className="habit-footer">
        <button
          className={`btn-complete ${habit.is_completed_today ? 'active' : ''}`}
          onClick={() => onToggleComplete(habit)}
        >
          {habit.is_completed_today ? '✓ Выполнено' : 'Отметить выполненным'}
        </button>
      </div>
    </div>
  )
}

export default HabitCard

