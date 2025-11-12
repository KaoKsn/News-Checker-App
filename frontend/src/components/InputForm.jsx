import React, { useState } from 'react';
import './InputForm.css'; // We'll create this file next for styling

function InputForm() {
  // 'useState' is a React Hook that lets our component remember things.
  // Here, we're creating a state variable to store the text the user types.
  const [inputValue, setInputValue] = useState('');

  // This function runs when the user submits the form (by clicking the button).
  const handleSubmit = async (event) => {
  event.preventDefault();
  console.log('Sending to backend:', inputValue);

  try {
    const response = await fetch('http://127.0.0.1:8000/check-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url: inputValue }),
    });

    const data = await response.json();
    console.log('Received from backend:', data);
    // Later, you'll use this data to display the result to the user!

  } catch (error) {
    console.error('Error sending data to backend:', error);
  }
};

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <label htmlFor="url-input" className="form-label">
          Enter a URL or Text to Check
        </label>
        <input
          type="text"
          id="url-input"
          className="form-input"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="e.g., https://x.com/username/status/12345"
          required
        />
        <button type="submit" className="form-button">
          Check Authenticity
        </button>
      </form>
    </div>
  );
}

export default InputForm;