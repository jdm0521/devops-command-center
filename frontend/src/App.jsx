import { useEffect, useState } from "react";

function App() {
  const [title, setTitle] = useState("");
  const [severity, setSeverity] = useState("");
  const [status, setStatus] = useState("");
  const [incidents, setIncidents] = useState([]); //incidents is the state value and setIncidents is how react updates that state. 
  const [changeRequests, setChangeRequests] = useState([]);

  

  useEffect(() => {
    fetch("http://localhost:8000/incidents")
      .then((response) => response.json())
      .then((data) => {
      console.log(data);
      setIncidents(data);
      });
  }, [])
      fetch("http://localhost:8000/change-requests")
      .then((response) => response.json())
      .then((data) => {
      setChangeRequests(data);
  });

  const createIncident = () => {
  fetch("http://localhost:8000/incidents", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title,
      severity,
      status,
    }),
  })
    .then((response) => response.json())
    .then((newIncident) => {
      setIncidents([...incidents, newIncident]);

      setTitle("");
      setSeverity("");
      setStatus("");
    });
  };

  return (
  <div className="container">
      <div className="header">
      <h1>DevOps Command Center</h1>
    <p>Enterprise Change & Incident Management Platform</p>
    </div>
    <h2>Create Incident</h2>

    <input
      type="text"
      placeholder="Title"
      value={title}
      onChange={(e) => setTitle(e.target.value)}
    />

    <input
      type="text"
      placeholder="Severity"
      value={severity}
      onChange={(e) => setSeverity(e.target.value)}
    />

    <input
      type="text"
      placeholder="Status"
      value={status}
      onChange={(e) => setStatus(e.target.value)}
    />

      <button onClick={createIncident}>
      Create Incident
      </button>

      <h2>Incidents</h2>
      <p>Total Incidents: {incidents.length}</p>
      <div>
        {incidents.map((incident) => (
      <div
      key={incident.id}
      className="card"

      >
      <h3>{incident.title}</h3>

      <p>Severity: {incident.severity}</p>

      <p>Status: {incident.status}</p>
    </div>
  ))}
  </div>
      <h2>Change Requests</h2>

  <div>
  {changeRequests.map((change) => (
    <div
      key={change.id}
      className="card"
    >
      <h3>{change.title}</h3>

      <p>Status: {change.status}</p>

      <p>Requested By: {change.requested_by}</p>
    </div>
  ))}
  </div>
    </div>
  );
}

export default App;