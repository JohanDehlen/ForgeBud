"""
ForgeBud

Project summary manager widget.

Displays and edits the project summary for an initialized ForgeBud
project. The widget contains presentation logic only and does not
access project files or services.
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from models.project_summary import ProjectSummary


class ProjectSummaryManagerWidget(QWidget):
    """
    Displays editable project-summary Markdown and emits save
    requests.
    """

    saveRequested = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self._create_ui()
        self._connect_signals()
        self.clear()
        self.disable_editing()

    def _create_ui(self) -> None:
        """
        Create and arrange the project-summary controls.
        """
        main_layout = QVBoxLayout(self)

        title_label = QLabel("Project Summary")
        main_layout.addWidget(title_label)

        self.summaryEditor = QTextEdit()
        self.summaryEditor.setAcceptRichText(False)
        self.summaryEditor.setPlaceholderText(
            "Open an initialized ForgeBud project to manage "
            "its project summary."
        )
        main_layout.addWidget(self.summaryEditor)

        self.saveButton = QPushButton(
            "Save Project Summary"
        )
        main_layout.addWidget(self.saveButton)

    def _connect_signals(self) -> None:
        """
        Connect internal controls to widget signals.
        """
        self.saveButton.clicked.connect(
            self._request_save
        )

    def set_project_summary(
        self,
        project_summary: ProjectSummary,
    ) -> None:
        """
        Display the supplied project-summary state.
        """
        self.summaryEditor.setPlainText(
            project_summary.markdown
        )

    def current_markdown(self) -> str:
        """
        Return the Markdown currently displayed by the editor.
        """
        return self.summaryEditor.toPlainText()

    def clear(self) -> None:
        """
        Clear the displayed project-summary document.
        """
        self.summaryEditor.clear()

    def enable_editing(self) -> None:
        """
        Enable project-summary editing and saving.
        """
        self.summaryEditor.setEnabled(True)
        self.saveButton.setEnabled(True)

    def disable_editing(self) -> None:
        """
        Disable project-summary editing and saving.
        """
        self.summaryEditor.setEnabled(False)
        self.saveButton.setEnabled(False)

    def _request_save(self) -> None:
        """
        Emit the current editor contents as a save request.
        """
        self.saveRequested.emit(
            self.current_markdown()
        )