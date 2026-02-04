from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                                 QLabel, QLineEdit, QPushButton, QComboBox, QGroupBox,
                                 QTextEdit, QSplitter, QFrame)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QPalette, QColor

class MainWindow(QMainWindow):
    # Signals to communicate with controller
    search_requested = Signal(str, str, str, str)  # mode, song_name, artist_name, link
    mode_changed = Signal(str)  # mode_text

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SpotiLeak - Music Search & Download")
        self.setGeometry(100, 100, 900, 700)
        self.setMinimumSize(600, 500)
        
        # Set up the main UI
        self.setup_ui()
        self.setup_style()
        
    def setup_ui(self):
        """Set up the main user interface"""
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title_label = QLabel("🎵 SpotiLeak")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)
        
        # Subtitle
        subtitle_label = QLabel("Download your favorite music from Spotify")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_font = QFont()
        subtitle_font.setPointSize(12)
        subtitle_label.setFont(subtitle_font)
        main_layout.addWidget(subtitle_label)
        
        # Mode selection
        mode_layout = QHBoxLayout()
        mode_label = QLabel("Search Mode:")
        mode_label.setMinimumWidth(100)
        
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Search by Song & Artist", "Search by YouTube Link"])
        self.mode_combo.currentTextChanged.connect(self.mode_changed.emit)
        self.mode_combo.setMinimumWidth(200)
        
        mode_layout.addWidget(mode_label)
        mode_layout.addWidget(self.mode_combo)
        mode_layout.addStretch()
        main_layout.addLayout(mode_layout)
        
        # Search input section
        self.search_group = QGroupBox("Search")
        self.search_group.setMinimumHeight(200)
        search_layout = QVBoxLayout(self.search_group)
        
        # Song & Artist input (default mode)
        self.song_artist_widget = QWidget()
        song_artist_layout = QVBoxLayout(self.song_artist_widget)
        
        # Song name input
        song_layout = QHBoxLayout()
        song_label = QLabel("Song Name:")
        song_label.setMinimumWidth(100)
        self.song_input = QLineEdit()
        self.song_input.setPlaceholderText("Enter song name...")
        song_layout.addWidget(song_label)
        song_layout.addWidget(self.song_input)
        song_artist_layout.addLayout(song_layout)
        
        # Artist name input
        artist_layout = QHBoxLayout()
        artist_label = QLabel("Artist Name:")
        artist_label.setMinimumWidth(100)
        self.artist_input = QLineEdit()
        self.artist_input.setPlaceholderText("Enter artist name...")
        artist_layout.addWidget(artist_label)
        artist_layout.addWidget(self.artist_input)
        song_artist_layout.addLayout(artist_layout)
        
        # Spotify link input (alternative mode)
        self.link_widget = QWidget()
        link_layout = QHBoxLayout(self.link_widget)
        link_label = QLabel("YouTube Link:")
        link_label.setMinimumWidth(100)
        self.link_input = QLineEdit()
        self.link_input.setPlaceholderText("Paste the YouTube link for the track here...")
        link_layout.addWidget(link_label)
        link_layout.addWidget(self.link_input)
        self.link_widget.setLayout(link_layout)
        
        # Add both widgets to search layout
        search_layout.addWidget(self.song_artist_widget)
        search_layout.addWidget(self.link_widget)
        
        # Search button
        button_layout = QHBoxLayout()
        self.search_button = QPushButton("🔍 Search & Download")
        self.search_button.setMinimumHeight(40)
        self.search_button.clicked.connect(self._emit_search_request)
        button_layout.addStretch()
        button_layout.addWidget(self.search_button)
        button_layout.addStretch()
        search_layout.addLayout(button_layout)
        
        main_layout.addWidget(self.search_group)
        
        # Results/Output section
        results_group = QGroupBox("Output")
        results_layout = QVBoxLayout(results_group)
        
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Search results and download progress will appear here...")
        self.output_text.setMinimumHeight(200)
        results_layout.addWidget(self.output_text)
        
        main_layout.addWidget(results_group)
        
        # Set initial mode
        self.update_mode_visibility("Search by Song & Artist")
        
        # Connect Enter key to search
        self.song_input.returnPressed.connect(self._emit_search_request)
        self.artist_input.returnPressed.connect(self._emit_search_request)
        self.link_input.returnPressed.connect(self._emit_search_request)
        
    def setup_style(self):
        """Apply custom styling to the UI"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            
            QLabel {
                color: #ffffff;
            }
            
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555555;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #1db954;
            }
            
            QLineEdit {
                background-color: #3c3c3c;
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 8px;
                font-size: 12px;
                color: #ffffff;
            }
            
            QLineEdit:focus {
                border-color: #1db954;
            }
            
            QComboBox {
                background-color: #3c3c3c;
                border: 2px solid #555555;
                border-radius: 6px;
                padding: 8px;
                font-size: 12px;
                color: #ffffff;
                min-width: 6em;
            }
            
            QComboBox:focus {
                border-color: #1db954;
            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #555555;
                border-left-style: solid;
                border-top-right-radius: 6px;
                border-bottom-right-radius: 6px;
            }
            
            QComboBox QAbstractItemView {
                background-color: #3c3c3c;
                color: #ffffff;
                selection-background-color: #1db954;
            }
            
            QPushButton {
                background-color: #1db954;
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                font-size: 14px;
                padding: 10px 20px;
                min-width: 150px;
            }
            
            QPushButton:hover {
                background-color: #1ed760;
            }
            
            QPushButton:pressed {
                background-color: #189945;
            }
            
            QTextEdit {
                background-color: #1a1a1a;
                border: 2px solid #555555;
                border-radius: 6px;
                color: #ffffff;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 11px;
                padding: 8px;
            }
        """)
        
    def _emit_search_request(self):
        """Emit search request signal with current input values"""
        self.search_requested.emit(
            self.mode_combo.currentText(),
            self.song_input.text(),
            self.artist_input.text(),
            self.link_input.text()
        )
            
    def update_mode_visibility(self, mode_text: str):
        """Update UI visibility based on selected mode"""
        if mode_text == "Search by Song & Artist":
            self.song_artist_widget.setVisible(True)
            self.link_widget.setVisible(False)
        else:  # "Search by YouTube Link"
            self.song_artist_widget.setVisible(False)
            self.link_widget.setVisible(True)
            
    def display_message(self, message: str, msg_type: str = "normal"):
        """Display a message in the output area with appropriate formatting"""
        if msg_type == "error":
            formatted_message = f"<span style='color: #ff6b6b;'>{message}</span>"
        elif msg_type == "success":
            formatted_message = f"<span style='color: #51cf66;'>{message}</span>"
        elif msg_type == "info":
            formatted_message = f"<span style='color: #74c0fc;'>{message}</span>"
        else:
            formatted_message = message
            
        self.output_text.append(formatted_message)
        
    def clear_output(self):
        """Clear the output area"""
        self.output_text.clear()
        
    def get_input_values(self) -> dict[str, str]:
        """Get current input values from the UI"""
        return {
            'mode': self.mode_combo.currentText(),
            'song_name': self.song_input.text().strip(),
            'artist_name': self.artist_input.text().strip(),
            'link': self.link_input.text().strip()
        }