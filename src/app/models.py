from dataclasses import dataclass
from typing import Optional

@dataclass
class SearchRequest:
    mode: str
    song_name: Optional[str] = None
    artist_name: Optional[str] = None
    link: Optional[str] = None

class SpotileakModel:
    def __init__(self):
        self.current_search: Optional[SearchRequest] = None
        self.search_results = []
        self.download_progress = 0
        
    def validate_search_request(self, request: SearchRequest) -> tuple[bool, str]:
        """Validate search request and return (is_valid, error_message)"""
        if request.mode == "Search by Song & Artist":
            if not request.song_name or not request.song_name.strip():
                return False, "Please enter a song name."
        else:  # YouTube Link mode
            if not request.link or not request.link.strip():
                return False, "Please enter a YouTube link."
            if "youtube.com" not in request.link.lower() and "youtu.be" not in request.link.lower():
                return False, "Please enter a valid YouTube link."
        return True, ""
    
    def set_current_search(self, request: SearchRequest):
        """Store the current search request"""
        self.current_search = request
        
    def clear_search_results(self):
        """Clear previous search results"""
        self.search_results.clear()
        
    def add_search_result(self, result):
        """Add a result to search results"""
        self.search_results.append(result)
        
    def update_download_progress(self, progress: int):
        """Update download progress"""
        self.download_progress = progress