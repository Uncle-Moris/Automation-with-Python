import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [data, setData] = useState('Loading...');
  const [buttonText, setButtonText] = useState('Click me');
  const [greeting, setGreeting] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setData(data.message);
      })
      .catch(err => {
        console.error('Error fetching data: ', err);
        setData('Failed to load data');
      });
  }, []);

  const handleClick = () => {
    setButtonText('Button Clicked!');
  };

  const handleGreetingClick = () => {
    fetch('http://localhost:5000/api/greeting')
      .then(response => response.json())
      .then(data => {
        setGreeting(data.message);
      })
      .catch(err => {
        console.error('Error fetching greeting: ', err);
        setGreeting('We have some troubles with the API.');
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>{data}</p>
        <button onClick={handleClick}>{buttonText}</button>
        <button onClick={handleGreetingClick}>Greetings</button>
        {greeting && <p>{greeting}</p>}
      </header>
    </div>
  );
}

export default App;
