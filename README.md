# SpotiLeak

Desktop app that downloads songs from YouTube and imports them into Spotify Local Files.

## Features
- Search YouTube for songs
- Preview videos in-app
- Download as high-quality MP3
- Auto-add metadata and album art
- Move to Spotify's local files folder

## Installation

**Install dependencies:**
```bash
# Install concurrently for npm scripts
npm install

# Install Python dependencies  
pip install -e .

# Install frontend dependencies
cd frontend && npm install
```

## Usage

**Option 1 - shell script:**
```bash
./start.sh
```

Both start backend (http://localhost:8000) and frontend (http://localhost:3000)

## Tech Stack
- **Frontend:** Electron + React + TypeScript
- **Backend:** Python + FastAPI + yt-dlp + mutagen