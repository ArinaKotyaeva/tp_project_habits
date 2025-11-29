import React, { useState, useEffect } from 'react'
import './HabitForm.css'

function HabitForm({ habit, onClose }) {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')

  useEffect(() => {
    if (habit) {
      setName(habit.name)
      setDescription(habit.description || '')
    }
  }, [habit])

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!name.trim()) {
      alert('Название привычки обязательно!')
      return
    }

    try {
      const url = habit
        ? `/api/habits/${habit.id}`
        : '/api/habits/'
      
      const method = habit ? 'PUT' : 'POST'
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name.trim(),
          description: description.trim() || null,
        }),
      })
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      onClose()
    } catch (error) {
      console.error('Error saving habit:', error)
      alert('Ошибка при сохранении привычки')
    }
  }

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>{habit ? 'Редактировать привычку' : 'Добавить привычку'}</h2>
          <button className="btn-close" onClick={onClose}>×</button>
        </div>
        
        <form onSubmit={handleSubmit} className="habit-form">
          <div className="form-group">
            <label htmlFor="name">Название привычки *</label>
            <input
              type="text"
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Например: Утренняя зарядка"
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="description">Описание</label>
            <textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Дополнительная информация о привычке"
              rows="4"
            />
          </div>
          
          <div className="form-actions">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Отмена
            </button>
            <button type="submit" className="btn btn-primary">
              {habit ? 'Сохранить' : 'Добавить'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default HabitForm

