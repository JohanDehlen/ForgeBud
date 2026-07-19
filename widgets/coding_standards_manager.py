"""
ForgeBud

Coding standards manager widget.

Displays and edits coding standards for an initialized ForgeBud
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

from models.coding_standards import CodingStandards


class CodingStandardsManagerWidget(QWidget):
    """
    Displays editable coding-standards Markdown and emits save
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
        Create and arrange the coding-standards controls.
        """
        main_layout = QVBoxLayout(self)

        title_label = QLabel("Coding Standards")
        main_layout.addWidget(title_label)

        self.standardsEditor = QTextEdit()
        self.standardsEditor.setAcceptRichText(False)
        self.standardsEditor.setPlaceholderText(
            "Open an initialized ForgeBud project to manage "
            "its coding standards."
        )
        main_layout.addWidget(self.standardsEditor)

        self.saveButton = QPushButton(
            "Save Coding Standards"
        )
        main_layout.addWidget(self.saveButton)

    def _connect_signals(self) -> None:
        """
        Connect internal controls to widget signals.
        """
        self.saveButton.clicked.connect(
            self._request_save
        )

    def set_coding_standards(
        self,
        coding_standards: CodingStandards,
    ) -> None:
        """
        Display the supplied coding-standards state.
        """
        self.standardsEditor.setPlainText(
            coding_standards.markdown
        )

    def current_markdown(self) -> str:
        """
        Return the Markdown currently displayed by the editor.
        """
        return self.standardsEditor.toPlainText()

    def clear(self) -> None:
        """
        Clear the displayed coding-standards document.
        """
        self.standardsEditor.clear()

    def enable_editing(self) -> None:
        """
        Enable coding-standards editing and saving.
        """
        self.standardsEditor.setEnabled(True)
        self.saveButton.setEnabled(True)

    def disable_editing(self) -> None:
        """
        Disable coding-standards editing and saving.
        """
        self.standardsEditor.setEnabled(False)
        self.saveButton.setEnabled(False)

    def _request_save(self) -> None:
        """
        Emit the current editor contents as a save request.
        """
        self.saveRequested.emit(
            self.current_markdown()
        )