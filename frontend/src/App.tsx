import React from "react";
import "./App.css";
import TypingText from "./components/TypingText.tsx";

function App(): React.JSX.Element {
  console.log("App component is rendering");
  const heroLines: string[] = [
    "Ever heard a song on social media that wasn't on Spotify?",
    "Listen to all the songs you love with SpotiLeak!"
  ]
  return (
    <div className="container">
      <div className="hero">
        <h1>SpotiLeak</h1>
        <TypingText lines={heroLines} speed={30} className="hero-text" />
      </div> 

      <div className="search-container">

      </div>
      
      <div className="results-container">

      </div>

      <div className="footer">

      </div>
    </div>
  );
}

export default App;