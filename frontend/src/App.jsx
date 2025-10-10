import React from 'react';
import InputForm from './components/InputForm';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>News Authenticity Checker</h1>
        <p>Verify information from social media and other sources.</p>
      </header>
      <main>
        <InputForm />
      </main>
    </div>
  );
}

export default App;