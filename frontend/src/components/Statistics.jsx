import React, { useState, useEffect } from 'react'
import { format, parseISO } from 'date-fns'
import './Statistics.css'

function Statistics() {
  const [viewMode, setViewMode] = useState('day') // 'day' or 'week'
  const [dayStats, setDayStats] = useState(null)
  const [weekStats, setWeekStats] = useState(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetchStatistics()
  }, [viewMode])

  const fetchStatistics = async () => {
    setLoading(true)
    try {
      if (viewMode === 'day') {
        const response = await fetch('/api/statistics/day')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        setDayStats(data)
      } else {
        const response = await fetch('/api/statistics/week')
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        setWeekStats(data)
      }
    } catch (error) {
      console.error('Error fetching statistics:', error)
    } finally {
      setLoading(false)
    }
  }

  const getProgressColor = (rate) => {
    if (rate >= 80) return '#2ed573'
    if (rate >= 50) return '#ffa502'
    return '#ff4757'
  }

  if (loading) {
    return (
      <div className="statistics-loading">
        <p>Загрузка статистики...</p>
      </div>
    )
  }

  return (
    <div className="statistics">
      <div className="statistics-header">
        <h2>Статистика</h2>
        <div className="view-toggle">
          <button
            className={`toggle-btn ${viewMode === 'day' ? 'active' : ''}`}
            onClick={() => setViewMode('day')}
          >
            День
          </button>
          <button
            className={`toggle-btn ${viewMode === 'week' ? 'active' : ''}`}
            onClick={() => setViewMode('week')}
          >
            Неделя
          </button>
        </div>
      </div>

      {viewMode === 'day' && dayStats && (
        <div className="day-statistics">
          <div className="stat-card">
            <h3>{format(parseISO(dayStats.date), 'd MMMM yyyy')}</h3>
            <div className="stat-metrics">
              <div className="metric">
                <span className="metric-label">Всего привычек</span>
                <span className="metric-value">{dayStats.total_habits}</span>
              </div>
              <div className="metric">
                <span className="metric-label">Выполнено</span>
                <span className="metric-value">{dayStats.completed_habits}</span>
              </div>
              <div className="metric">
                <span className="metric-label">Процент выполнения</span>
                <span
                  className="metric-value"
                  style={{ color: getProgressColor(dayStats.completion_rate) }}
                >
                  {dayStats.completion_rate}%
                </span>
              </div>
            </div>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${dayStats.completion_rate}%`,
                  backgroundColor: getProgressColor(dayStats.completion_rate),
                }}
              />
            </div>
          </div>
        </div>
      )}

      {viewMode === 'week' && weekStats && (
        <div className="week-statistics">
          <div className="stat-card">
            <h3>
              {format(parseISO(weekStats.week_start), 'd MMM')} -{' '}
              {format(parseISO(weekStats.week_end), 'd MMM yyyy')}
            </h3>
            <div className="stat-metrics">
              <div className="metric">
                <span className="metric-label">Всего привычек</span>
                <span className="metric-value">{weekStats.total_habits}</span>
              </div>
              <div className="metric">
                <span className="metric-label">Выполнено за неделю</span>
                <span className="metric-value">{weekStats.completed_habits}</span>
              </div>
              <div className="metric">
                <span className="metric-label">Процент выполнения</span>
                <span
                  className="metric-value"
                  style={{ color: getProgressColor(weekStats.completion_rate) }}
                >
                  {weekStats.completion_rate}%
                </span>
              </div>
            </div>
            <div className="progress-bar">
              <div
                className="progress-fill"
                style={{
                  width: `${weekStats.completion_rate}%`,
                  backgroundColor: getProgressColor(weekStats.completion_rate),
                }}
              />
            </div>
          </div>

          <div className="daily-stats">
            <h4>Статистика по дням</h4>
            <div className="daily-stats-grid">
              {weekStats.daily_stats.map((day) => (
                <div key={day.date} className="daily-stat-card">
                  <div className="daily-stat-header">
                    <span className="day-name">
                      {format(parseISO(day.date), 'EEE')}
                    </span>
                    <span className="day-date">
                      {format(parseISO(day.date), 'd MMM')}
                    </span>
                  </div>
                  <div className="daily-stat-metrics">
                    <span className="daily-completed">
                      {day.completed_habits}/{day.total_habits}
                    </span>
                    <span
                      className="daily-rate"
                      style={{ color: getProgressColor(day.completion_rate) }}
                    >
                      {day.completion_rate}%
                    </span>
                  </div>
                  <div className="daily-progress-bar">
                    <div
                      className="daily-progress-fill"
                      style={{
                        width: `${day.completion_rate}%`,
                        backgroundColor: getProgressColor(day.completion_rate),
                      }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default Statistics

