"""
ForgeBud

Project initializer dialog.

Collects editable project metadata before ForgeBud project
initialization. The dialog contains presentation logic only and does
not access project files or services.
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from models.project_info import ProjectInfo


class ProjectInitializerDialog(QDialog):
    """
    Collects project information for ForgeBud initialization.
    """

    def __init__(
        self,
        project_info: ProjectInfo,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        self.setWindowTitle("Initialize ForgeBud")
        self.setModal(True)
        self.resize(560, 420)

        self._create_ui()
        self._connect_signals()
        self.set_project_info(project_info)

    def _create_ui(self) -> None:
        """
        Create and arrange the initialization controls.
        """
        main_layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.nameEdit = QLineEdit()
        self.versionEdit = QLineEdit()

        self.descriptionEdit = QTextEdit()
        self.descriptionEdit.setAcceptRichText(False)
        self.descriptionEdit.setMinimumHeight(100)

        self.languageEdit = QLineEdit()
        self.frameworkEdit = QLineEdit()
        self.repositoryEdit = QLineEdit()

        form_layout.addRow("Project Name", self.nameEdit)
        form_layout.addRow("Version", self.versionEdit)
        form_layout.addRow("Description", self.descriptionEdit)
        form_layout.addRow("Language", self.languageEdit)
        form_layout.addRow("Framework", self.frameworkEdit)
        form_layout.addRow("Repository", self.repositoryEdit)

        main_layout.addLayout(form_layout)

        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok
            | QDialogButtonBox.StandardButton.Cancel
        )
        main_layout.addWidget(self.buttonBox)

    def _connect_signals(self) -> None:
        """
        Connect dialog actions.
        """
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def set_project_info(
        self,
        project_info: ProjectInfo,
    ) -> None:
        """
        Populate the dialog from project-information state.
        """
        self.nameEdit.setText(project_info.name)
        self.versionEdit.setText(project_info.version)
        self.descriptionEdit.setPlainText(
            project_info.description
        )
        self.languageEdit.setText(project_info.language)
        self.frameworkEdit.setText(project_info.framework)
        self.repositoryEdit.setText(project_info.repository)

    def project_info(self) -> ProjectInfo:
        """
        Return project-information state entered in the dialog.
        """
        return ProjectInfo(
            name=self.nameEdit.text(),
            version=self.versionEdit.text(),
            description=self.descriptionEdit.toPlainText(),
            language=self.languageEdit.text(),
            framework=self.frameworkEdit.text(),
            repository=self.repositoryEdit.text(),
        )