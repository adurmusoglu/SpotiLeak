# SpotiLeak

A native desktop app that helps you take local music files and make them usable in Spotify via Local Files.

You search for a song, preview it on YouTube to confirm it's the right one, then import an audio file for the . SpotiLeak automatically:

- **Finds the song you want on YouTube**
- **Gives you the option to download the song or keep searching if desired**
- **Fills in song metadata**
- **Embeds album artwork**  
- **Moves the file into a folder Spotify watches**

## For Non-Programmers (Start Here)

### What SpotiLeak Does

- Helps you organize and tag local music
- Makes tracks appear cleanly in Spotify under Local Files
- Lets you preview songs before importing

### How to Use SpotiLeak

1. **Open SpotiLeak**
2. **Search** for a song (artist + title)
3. **Preview** results using the built-in player
4. **Choose** to download the song as MP3 if satisfied
5. **Confirm** or edit metadata
6. **Click** Save to Spotify
7. **Open** Spotify → Local Files

**That's it!**

> **Tip:** If the song doesn't appear immediately, restart Spotify. Spotify can be glitchy with files appearing in local files, and even glitchier with it appearing on other devices. Troubleshooting tips for this are included in the main menu of the application.

### Spotify Setup (One-Time)

1. Open **Spotify Desktop**
2. Go to **Settings**
3. Enable **Local Files**
4. Add the folder SpotiLeak uses
5. Restart Spotify

## Features

- **Native desktop app** (no browser needed)
- **YouTube search & preview** (official APIs)
- **Local MP3 ingestion**
- **Automatic ID3 tagging:**
  - Artist
  - Song title
  - Album (defaults supported)
  - 300×300 embedded album art
- **Automatic copy/move** to Spotify folder
- **Tracks remembered** in a local database

## Technical Overview (For Developers)

### Tech Stack

- **Language:** Python 3.10+
- **UI:** PySide6 (Qt)
- **Preview Player:** YouTube IFrame Player API (QWebEngineView)
- **Search API:** YouTube Data API v3
- **Tagging:** mutagen
- **Images:** Pillow
- **Database:** SQLite  

### Project Structure

```
spotileak/
├── src/
│   └── spotileak/
│       ├── app.py                 # App entry point
│       ├── ui/                    # Qt UI components
│       ├── core/                  # config, db, models
│       ├── services/              # YouTube search, tagging, file handling
│       └── web/                   # embedded YouTube player
├── data/
│   └── app.db                     # runtime database
└── tests/
```

## Setup (Developers Only)

### Requirements

- Python 3.10+
- Spotify Desktop App
- YouTube Data API key

### Install

```bash
pip install -r requirements.txt
```

### Environment Variables

Create `.env`:

```env
YOUTUBE_API_KEY=your_api_key_here
```

## Known Limitations

- Spotify controls Local Files behavior
- Metadata refresh may require restarting Spotify
- Mobile Local Files sync is unreliable
- Only MP3 is supported initially

## Disclaimer

SpotiLeak manages local audio files only.
It does not upload content to Spotify automatically. 