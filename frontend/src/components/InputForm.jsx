import React, { useState } from 'react';
import './InputForm.css'; // We'll create this file next for styling

function InputForm() {
  // 'useState' is a React Hook that lets our component remember things.
  // Here, we're creating a state variable to store the text the user types.
  const [inputValue, setInputValue] = useState('');

  // This function runs when the user submits the form (by clicking the button).
  const handleSubmit = (event) => {
    // This prevents the browser from doing a full page refresh.
    event.preventDefault();

    // For now, we'll just print the input to the browser's developer console.
    // Later, this is where you'll send the data to your backend API!
    console.log('Submitting URL or text:', inputValue);
    // You could add logic here to show a "Loading..." message.
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