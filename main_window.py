from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QWidget,
)

from version import APP_NAME, APP_VERSION

from models.project_info import ProjectInfo

from widgets.project_panel import ProjectPanel
from widgets.status_bar import StatusBar

from services.git_service import GitService
from services.project_service import ProjectService


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.projectPath: Path | None = None

        self.setWindowTitle(f"{APP_NAME} v{APP_VERSION}")
        self.resize(1200, 800)

        # -------------------------------------------------
        # Central Widget
        # -------------------------------------------------

        central = QWidget()

        self.setCentralWidget(central)

        mainLayout = QVBoxLayout(central)

        # -------------------------------------------------
        # Main Content
        # -------------------------------------------------

        contentLayout = QHBoxLayout()

        self.projectPanel = ProjectPanel()

        contentLayout.addWidget(self.projectPanel)

        mainLayout.addLayout(contentLayout)

        # -------------------------------------------------
        # Status Bar
        # -------------------------------------------------

        self.statusBarWidget = StatusBar()

        mainLayout.addWidget(self.statusBarWidget)

        # -------------------------------------------------
        # Signals
        # -------------------------------------------------

        self.projectPanel.openButton.clicked.connect(
            self.open_project
        )

        self.projectPanel.initializeButton.clicked.connect(
            self.initialize_project
        )

    # =====================================================
    # Project
    # =====================================================

    def open_project(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Open Project",
        )

        if not folder:
            return

        self.load_project(folder)

    def load_project(self, folder):

        self.projectPath = Path(folder)

        self.statusBarWidget.setText(
            f"Opened project: {self.projectPath.name}"
        )

        #
        # Git
        #

        if GitService.is_repository(folder):

            branch = GitService.current_branch(folder)

            self.projectPanel.set_repository_status(
                f"Git Repository ({branch})"
            )

        else:

            self.projectPanel.set_repository_status(
                "Not a Git repository"
            )

        #
        # ForgeBud
        #

        if ProjectService.is_initialized(folder):

            info = ProjectService.load(folder)

            self.projectPanel.set_project(info)

            self.projectPanel.disable_initialize()

            self.statusBarWidget.setText(
                "ForgeBud project loaded."
            )

        else:

            self.projectPanel.clear()

            self.projectPanel.set_repository_status(
                "Project not initialized"
            )

            self.projectPanel.enable_initialize()

            self.statusBarWidget.setText(
                "Project ready for initialization."
            )

    def initialize_project(self):

        if self.projectPath is None:

            QMessageBox.information(
                self,
                "No Project",
                "Please open a project first.",
            )

            return

        info = ProjectInfo()

        info.name = self.projectPath.name
        info.version = "0.1.0"
        info.description = ""
        info.language = "Python"
        info.framework = "Unknown"

        ProjectService.initialize(
            self.projectPath,
            info,
        )

        self.load_project(self.projectPath)

        QMessageBox.information(
            self,
            "ForgeBud",
            "Project initialized successfully.",
        )

        self.statusBarWidget.setText(
            "Project initialized successfully."
        )