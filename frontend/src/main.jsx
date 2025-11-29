import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

try {
  const rootElement = document.getElementById('root')
  if (!rootElement) {
    throw new Error('Root element not found!')
  }
  
  ReactDOM.createRoot(rootElement).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
  )
} catch (error) {
  console.error('Error rendering app:', error)
  document.body.innerHTML = `
    <div style="padding: 20px; font-family: Arial;">
      <h1>Ошибка загрузки приложения</h1>
      <p>${error.message}</p>
      <p>Проверьте консоль браузера (F12) для подробностей.</p>
    </div>
  `
}

