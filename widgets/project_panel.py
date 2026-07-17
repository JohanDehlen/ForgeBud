from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QFrame,
)

from models.project_info import ProjectInfo


class ProjectPanel(QWidget):
    """
    Displays information about the currently
    opened project.
    """

    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout(self)

        # -------------------------------------------------
        # Project Information
        # -------------------------------------------------

        form = QFormLayout()

        self.nameLabel = QLabel("-")
        self.versionLabel = QLabel("-")
        self.languageLabel = QLabel("-")
        self.frameworkLabel = QLabel("-")
        self.repositoryLabel = QLabel("No Project Loaded")

        form.addRow("Project", self.nameLabel)
        form.addRow("Version", self.versionLabel)
        form.addRow("Language", self.languageLabel)
        form.addRow("Framework", self.frameworkLabel)
        form.addRow("Repository", self.repositoryLabel)

        mainLayout.addLayout(form)

        # -------------------------------------------------
        # Separator
        # -------------------------------------------------

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)

        mainLayout.addWidget(separator)

        # -------------------------------------------------
        # Project Actions
        # -------------------------------------------------

        buttonLayout = QHBoxLayout()

        self.openButton = QPushButton("Open Project")

        self.initializeButton = QPushButton(
            "Initialize ForgeBud"
        )

        self.initializeButton.setEnabled(False)

        buttonLayout.addWidget(self.openButton)
        buttonLayout.addWidget(self.initializeButton)

        mainLayout.addLayout(buttonLayout)

        mainLayout.addStretch()

    # -------------------------------------------------
    # Public API
    # -------------------------------------------------

    def clear(self):
        """
        Clears the displayed project information.
        """

        self.nameLabel.setText("-")
        self.versionLabel.setText("-")
        self.languageLabel.setText("-")
        self.frameworkLabel.setText("-")
        self.repositoryLabel.setText("No Project Loaded")

        self.initializeButton.setEnabled(False)

    def set_project(self, info: ProjectInfo):
        """
        Display project metadata.
        """

        self.nameLabel.setText(info.name or "-")
        self.versionLabel.setText(info.version or "-")
        self.languageLabel.setText(info.language or "-")
        self.frameworkLabel.setText(info.framework or "-")

    def set_repository_status(self, text: str):
        """
        Update repository status.
        """

        self.repositoryLabel.setText(text)

    def enable_initialize(self):
        """
        Enable the Initialize button.
        """

        self.initializeButton.setEnabled(True)

    def disable_initialize(self):
        """
        Disable the Initialize button.
        """

        self.initializeButton.setEnabled(False)