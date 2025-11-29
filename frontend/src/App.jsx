import React, { useState, useEffect } from 'react'
import HabitsList from './components/HabitsList'
import HabitForm from './components/HabitForm'
import Statistics from './components/Statistics'
import './App.css'

function App() {
  const [habits, setHabits] = useState([])
  const [showForm, setShowForm] = useState(false)
  const [editingHabit, setEditingHabit] = useState(null)
  const [activeTab, setActiveTab] = useState('habits')

  useEffect(() => {
    fetchHabits()
  }, [])

  const fetchHabits = async () => {
    try {
      const response = await fetch('/api/habits/')
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const data = await response.json()
      setHabits(data)
    } catch (error) {
      alert('Не удалось загрузить привычки. Убедитесь, что backend сервер запущен на порту 8000.')
    }
  }

  const handleAddHabit = () => {
    setEditingHabit(null)
    setShowForm(true)
  }

  const handleEditHabit = (habit) => {
    setEditingHabit(habit)
    setShowForm(true)
  }

  const handleFormClose = () => {
    setShowForm(false)
    setEditingHabit(null)
    fetchHabits()
  }

  const handleDeleteHabit = async (id) => {
    if (window.confirm('Вы уверены, что хотите удалить эту привычку?')) {
      try {
        await fetch(`/api/habits/${id}`, {
          method: 'DELETE',
        })
        fetchHabits()
      } catch (error) {
      }
    }
  }

  const handleToggleComplete = async (habit) => {
    try {
      if (habit.is_completed_today) {
        await fetch(`/api/habits/${habit.id}/complete`, {
          method: 'DELETE',
        })
      } else {
        await fetch(`/api/habits/${habit.id}/complete`, {
          method: 'POST',
        })
      }
      fetchHabits()
    } catch (error) {
    }
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>Учёт привычек</h1>
          <div className="tabs">
            <button
              className={`tab ${activeTab === 'habits' ? 'active' : ''}`}
              onClick={() => setActiveTab('habits')}
            >
              Привычки
            </button>
            <button
              className={`tab ${activeTab === 'statistics' ? 'active' : ''}`}
              onClick={() => setActiveTab('statistics')}
            >
              Статистика
            </button>
          </div>
        </header>

        {activeTab === 'habits' && (
          <main className="main">
            <div className="habits-header">
              <h2>Мои привычки</h2>
              <button className="btn btn-primary" onClick={handleAddHabit}>
                + Добавить привычку
              </button>
            </div>

            <HabitsList
              habits={habits}
              onEdit={handleEditHabit}
              onDelete={handleDeleteHabit}
              onToggleComplete={handleToggleComplete}
            />

            {showForm && (
              <HabitForm
                habit={editingHabit}
                onClose={handleFormClose}
              />
            )}
          </main>
        )}

        {activeTab === 'statistics' && (
          <Statistics />
        )}
      </div>
    </div>
  )
}

export default App

