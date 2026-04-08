import { useState, useEffect } from 'react'

function App() {
  const [todos, setTodos] = useState([])
  const [newTitle, setNewTitle] = useState('')
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchTodos()
  }, [])

  function fetchTodos() {
    fetch('/todos')
      .then(res => {
        if (!res.ok) throw new Error(`GET /todos failed: ${res.status}`)
        return res.json()
      })
      .then(data => setTodos(data))
      .catch(err => setError(err.message))
  }

  function addTodo(e) {
    e.preventDefault()
    if (!newTitle.trim()) return
    fetch('/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: newTitle })
    })
      .then(res => {
        if (!res.ok) throw new Error(`POST /todos failed: ${res.status}`)
        setNewTitle('')
        fetchTodos()
      })
      .catch(err => setError(err.message))
  }

  return (
    <div style={{ maxWidth: 500, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h1>Todo App</h1>

      {error && (
        <p style={{ color: 'red', background: '#fee', padding: 8, borderRadius: 4 }}>
          Error: {error}
        </p>
      )}

      <form onSubmit={addTodo} style={{ display: 'flex', gap: 8, marginBottom: 24 }}>
        <input
          value={newTitle}
          onChange={e => setNewTitle(e.target.value)}
          placeholder="New task..."
          style={{ flex: 1, padding: '8px 12px', fontSize: 16 }}
        />
        <button type="submit" style={{ padding: '8px 16px', fontSize: 16 }}>
          Add
        </button>
      </form>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {todos.map(todo => (
          <li
            key={todo.id}
            style={{
              padding: '10px 12px',
              borderBottom: '1px solid #eee',
              textDecoration: todo.done ? 'line-through' : 'none',
              color: todo.done ? '#aaa' : '#000'
            }}
          >
            {todo.title}
          </li>
        ))}
      </ul>

      {todos.length === 0 && <p style={{ color: '#999' }}>No tasks yet.</p>}
    </div>
  )
}

export default App
