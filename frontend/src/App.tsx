import React, { useState } from "react";
import "./App.css";
import TypingText from "./components/TypingText.tsx";
import SearchInput from "./components/SearchInput.tsx";

function App(): React.JSX.Element {
  console.log("App component is rendering");
  const [artistQuery, setArtistQuery] = useState('');
  const [songQuery, setSongQuery] = useState('');
  const heroLines: string[] = [
    "Ever heard a song on social media that wasn't on Spotify?",
    "Listen to all the songs you love with SpotiLeak!"
  ]
  return (
    <div className="container">
      <div className="hero">
        <h1>SpotiLeak</h1>
        <TypingText lines={heroLines} speed={25} className="hero-text" />
      </div> 

      <div className="search-container">
        <SearchInput type="artist" value={artistQuery} onChange={setArtistQuery} />
        <SearchInput type="song" value={songQuery} onChange={setSongQuery} />
        <button className="btn-search">Search</button>
      </div>
      
      <div className="helper-info">
        { /* insert recent searches vertical left side, tutorial/helper info such
          as how to actually link, troubleshooting, setup, etc. on right vertical side */ }
      </div>

      <div className="footer">

      </div>
    </div>
  );
}

export default App;