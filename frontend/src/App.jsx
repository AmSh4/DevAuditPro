import React, {useEffect, useState} from 'react'

export default function App(){
  const [audits, setAudits] = useState([])
  useEffect(()=>{
    fetch('/api/audits/')
      .then(r=>r.json())
      .then(setAudits)
      .catch(()=>setAudits([]))
  },[])
  return (
    <div className="app">
      <header><h1>DevAuditPro</h1></header>
      <main>
        <section className="card">
          <h2>Recent Audits</h2>
          <ul>
            {audits.length===0 && <li>No audits yet (run backend scan first)</li>}
            {audits.map(a=>(
              <li key={a.id}>{a.repo_name} — score: {a.score} — {a.summary}</li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  )
}
