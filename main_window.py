"""
ForgeFlow

Main application window.

Responsibilities:
- Create and arrange widgets.
- Connect widget signals.
- Coordinate application workflow.

Business logic belongs in services.
"""

from PySide6.QtCore import QPoint, QSize
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from services.settings_service import SettingsService
from version import (
    APP_DESCRIPTION,
    APP_NAME,
    WINDOW_TITLE,
)
from widgets.project_panel import ProjectPanel
from widgets.status_bar import StatusBar


class MainWindow(QMainWindow):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.settings = SettingsService.load()

        self.setWindowTitle(WINDOW_TITLE)

        self._restore_window()

        self._build_ui()

        self._load_settings()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def _build_ui(self) -> None:

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        #
        # Header
        #

        title = QLabel(APP_NAME)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        subtitle = QLabel(APP_DESCRIPTION)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        #
        # Project Panel
        #

        self.projectPanel = ProjectPanel()

        layout.addWidget(self.projectPanel)

        #
        # Stretch
        #

        layout.addStretch()

        #
        # Status Bar
        #

        self.statusBarWidget = StatusBar()

        layout.addWidget(self.statusBarWidget)

        #
        # Signals
        #

        self.projectPanel.projectChanged.connect(
            self._project_changed
        )

    # -------------------------------------------------
    # Settings
    # -------------------------------------------------

    def _restore_window(self) -> None:

        width = self.settings["window_width"]
        height = self.settings["window_height"]

        self.resize(QSize(width, height))

        if (
            self.settings["window_x"] is not None
            and
            self.settings["window_y"] is not None
        ):
            self.move(
                QPoint(
                    self.settings["window_x"],
                    self.settings["window_y"],
                )
            )

    def _load_settings(self) -> None:

        project = self.settings.get(
            "last_project",
            "",
        )

        if project:

            self.projectPanel.set_project_path(project)

            self.statusBarWidget.show_message(
                "Last project restored."
            )

    def _save_settings(self) -> None:

        self.settings["last_project"] = (
            self.projectPanel.project_path()
        )

        self.settings["window_width"] = self.width()
        self.settings["window_height"] = self.height()

        self.settings["window_x"] = self.x()
        self.settings["window_y"] = self.y()

        SettingsService.save(self.settings)

    # -------------------------------------------------
    # Events
    # -------------------------------------------------

    def _project_changed(self, project: str) -> None:

        self.statusBarWidget.show_message(
            f"Project selected: {project}"
        )

        self._save_settings()

    def closeEvent(self, event):

        self._save_settings()

        super().closeEvent(event)