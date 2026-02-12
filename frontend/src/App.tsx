import React, { useState } from "react";
import "./App.css";
import "./types/api.tsx";
import TypingText from "./components/TypingText.tsx";
import SearchInput from "./components/SearchInput.tsx";


function App(): React.JSX.Element {
  console.log("App component is rendering");
  // Handles data search queries
  const [artistQuery, setArtistQuery] = useState('');
  const [songQuery, setSongQuery] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  let search_data: any = null;
  let query_id: number = 0;  

  // Customizable hero text with animation
  const heroLines: string[] = [
    "Ever heard a song on social media that wasn't on Spotify?",
    "Listen to all the songs you love with SpotiLeak!"
  ]

  // Handles the UI serach interactions for song/artist names
  const handleSearch = async () => {
    // Prevents double-click searches
    if (isSearching) { return; }
    setIsSearching(true);
    // Basic validation 
    if (!songQuery.trim()) {
      alert("Song name is required!");
      return;
    }

    console.log("Sending search request:", {artist: artistQuery, song: songQuery });

    try {
      // Send search request to backend
      const response = await fetch("http://localhost:8000/api/search",{
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          song: songQuery.trim(),
          artist: artistQuery.trim(),
          total_results: 10,
          query_id: query_id++
        })
      });
      console.log("Response status:", response.status);

      search_data = await response.json();
      console.log("Response data:", search_data);
    } catch (err) {
      console.error("Search request failed.", err);
    } finally {
      setIsSearching(false);
    }
  }
  return (
    <div className="container">
      <div className="hero">
        <h1>SpotiLeak</h1>
        <TypingText lines={heroLines} speed={25} className="hero-text" />
      </div> 

      <div className="search-container">
        <SearchInput type="song" value={songQuery} onChange={setSongQuery} />
        <SearchInput type="artist" value={artistQuery} onChange={setArtistQuery} />
        <button className="btn-search" onClick={handleSearch}>Search</button>
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