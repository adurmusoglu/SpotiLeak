from PySide6.QtCore import QObject, Signal
from .models import SpotileakModel, SearchRequest
from .ui import MainWindow

class SpotileakController(QObject):
    # Signals for communicating with external services
    search_song_requested = Signal(str, str)  # song_name, artist_name
    search_link_requested = Signal(str)       # link
    
    def __init__(self):
        super().__init__()
        self.model = SpotileakModel()
        self.view = MainWindow()
        
        # Connect view signals to controller methods
        self.view.search_requested.connect(self.handle_search_request)
        self.view.mode_changed.connect(self.handle_mode_change)
        
    def handle_search_request(self, mode: str, song_name: str, artist_name: str, link: str):
        """Handle search request from the UI"""
        # Create search request model
        request = SearchRequest(
            mode=mode,
            song_name=song_name.strip() if song_name else None,
            artist_name=artist_name.strip() if artist_name else None,
            link=link.strip() if link else None
        )
        
        # Validate the request
        is_valid, error_msg = self.model.validate_search_request(request)
        if not is_valid:
            self.view.display_message(error_msg, "error")
            return
            
        # Store the request in model
        self.model.set_current_search(request)
        
        # Clear previous results
        self.model.clear_search_results()
        self.view.clear_output()
        
        # Perform the search based on mode
        if request.mode == "Search by Song & Artist":
            self.view.display_message(
                f"🔍 Searching for: '{request.song_name}' by '{request.artist_name}'...", 
                "info"
            )
            # Emit signal for external search service to handle
            self.search_song_requested.emit(request.song_name, request.artist_name or "")
            
        else:  # YouTube Link mode
            self.view.display_message(f"🔍 Processing YouTube link: {request.link}", "info")
            # Emit signal for external search service to handle
            self.search_link_requested.emit(request.link)
            
    def handle_mode_change(self, mode_text: str):
        """Handle mode change in the UI"""
        self.view.update_mode_visibility(mode_text)
        
    def display_search_result(self, message: str, msg_type: str = "success"):
        """Display search results in the UI"""
        self.view.display_message(message, msg_type)
        
    def display_error(self, error_message: str):
        """Display error message in the UI"""
        self.view.display_message(error_message, "error")
        
    def display_info(self, info_message: str):
        """Display info message in the UI"""
        self.view.display_message(info_message, "info")
        
    def update_download_progress(self, progress: int, message: str = None):
        """Update download progress"""
        self.model.update_download_progress(progress)
        if message:
            self.view.display_message(message, "info")
            
    def get_view(self) -> MainWindow:
        """Get the view instance"""
        return self.view