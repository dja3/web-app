import React from 'react';
import logo from './austie_face.png';
import './App.css';

const API_BASE_URL = process.env.REACT_APP_APP_SERVER;
const API_BASE_URL_PORT = process.env.REACT_APP_APP_SERVER_PORT;

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Austin's {" "}
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=vnfSqlF5LHE"
          target="_blank"
          rel="noopener noreferrer"
        >
          Billion
        </a>
          {" "}Dollar Idea List
        </p>
        <img src={logo} className="App-logo" alt="logo" />
        <p>

        </p>
      </header>
    </div>
  );
}

export default App;
