import React from 'react'
import HabitCard from './HabitCard'
import './HabitsList.css'

function HabitsList({ habits, onEdit, onDelete, onToggleComplete }) {
  if (habits.length === 0) {
    return (
      <div className="empty-state">
        <p>У вас пока нет привычек. Добавьте первую!</p>
      </div>
    )
  }

  return (
    <div className="habits-list">
      {habits.map((habit) => (
        <HabitCard
          key={habit.id}
          habit={habit}
          onEdit={onEdit}
          onDelete={onDelete}
          onToggleComplete={onToggleComplete}
        />
      ))}
    </div>
  )
}

export default HabitsList

