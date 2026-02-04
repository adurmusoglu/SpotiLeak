import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

try:
    from .controller import SpotileakController
except ImportError:
    from controller import SpotileakController


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("SpotiLeak")
    app.setApplicationVersion("0.1.0")
    
    # Set app icon
    icon_path = Path(__file__).parent / "resources" / "icon.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    
    # Create controller (which creates model and view)
    controller = SpotileakController()
    
    # Show the view
    controller.get_view().show()
    
    return app.exec()