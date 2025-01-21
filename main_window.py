import os
import json
from PyQt5 import uic
from pathlib import Path
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QFileDialog, QDialog, QGraphicsDropShadowEffect


class APIKEY(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/api_key_dialog.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.btnClose.clicked.connect(self.close)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.setGraphicsEffect(self.shadow)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main_window.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        self.create_program_directory()
        self.populateProjectComboBox()
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        self.btnClose.clicked.connect(self.close)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btnCommit.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.commitPage)
        )
        self.btnPullRequest.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pullRequestPage)
        )
        self.btnSettings.clicked.connect(self.open_dialog)

        self.btnBrowse.clicked.connect(self.browseProjectFolder)

        self.btnRemoveProject.clicked.connect(self.on_remove_roject)

        self.btnSaveProjectConfiguration.clicked.connect(self.saveProjectConfiguration)
        self.setExtentionsFont()

        self.projectsComboBox.currentIndexChanged.connect(self.on_combo_box_changed)

    def open_dialog(self):
        self.dialog = APIKEY()
        self.dialog.show()

    def setExtentionsFont(self):
        font = QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(15)  # Set font size to 14
        self.fileExtentionsTextEdit.setFont(font)
        self.fileExtentionsTextEdit.clear()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

    def browseProjectFolder(self):
        dialog_title = "Select Project Folder"
        path = QFileDialog.getExistingDirectory(self, dialog_title)
        if path:
            try:
                self.projectPath.setText(path)
                self.projectKey.setText(self.get_path_basename(path))
            except Exception as e:
                self.projectPathsetText(str(e))
        return path

    def saveProjectConfiguration(self):
        project_name = self.projectKey.text()
        project_path = self.projectPath.text()
        file_extensions = self.fileExtentionsTextEdit.toPlainText().strip()
        self.append_to_json(
            self.projectsJson(), project_name, project_path, file_extensions
        )
        self.populateProjectComboBox()

    def get_path_basename(self, path: str) -> str:
        return os.path.basename(path)

    def create_program_directory(self):
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)
            json_path = os.path.join(root_dir, "projects.json")
            json_path = Path(json_path)
            json_api = os.path.join(root_dir, "apiKey.json")
            json_api = Path(json_api)
            json_api.touch(exist_ok=True)
            json_path.touch(exist_ok=True)

    def apiKeyPath(self):
        # Determine root directory based on OS
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        json_path = Path(root_dir) / "apiKey.json"
        return json_path

    def projectsJson(self):
        # Determine root directory based on OS
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        json_path = Path(root_dir) / "projects.json"
        return json_path

    def is_git_repository(self, folder_path):
        """
        Check if the given folder is a Git repository.
        """
        git_dir = os.path.join(folder_path, ".git")
        if os.path.isdir(git_dir):
            return True
        return False

    def append_to_json(
        self, file_path: str, project_name: str, path: str, extensions: str
    ):
        """
        Append or update a project entry in a JSON file where the project name is the key.
        If the file is empty or invalid, create a new dictionary.
        """
        # Check if the file exists and is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            # Load existing JSON data
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                    # Ensure it's a dictionary, reset if not
                    if not isinstance(data, dict):
                        data = {}
                except json.JSONDecodeError:
                    data = {}  # Initialize as an empty dictionary if invalid JSON
        else:
            data = (
                {}
            )  # Initialize as an empty dictionary if file doesn't exist or is empty

        # Create or update the entry for the project
        data[project_name] = {"path": path, "extensions": extensions}

        # Write the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def get_json_keys(self, file_path: str) -> list:
        """
        Load a JSON file from the given path and return a list of its keys.

        :param file_path: Path to the JSON file
        :return: List of keys in the JSON file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file at {file_path} does not exist.")

        with open(file_path, "r") as file:
            try:
                # Load JSON data
                json_data = json.load(file)

                # Ensure it's a dictionary
                if isinstance(json_data, dict):
                    return list(json_data.keys())
                else:
                    raise ValueError(
                        "The JSON file does not contain a dictionary at the root level."
                    )
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")

    def populateProjectComboBox(self):
        self.projectsComboBox.clear()
        path = self.get_json_keys(self.projectsJson())
        self.projectsComboBox.addItems(path)

    def on_combo_box_changed(self):
        try:
            self.fileExtentionsTextEdit.clear()
            selected_item = self.projectsComboBox.currentText()
            item = self.get_item_by_key(selected_item)
            self.projectPath.setText(item['path'])
            self.projectKey.setText(selected_item)
            self.fileExtentionsTextEdit.append(item['extensions'])
        except Exception as e:
            print(f'An exception occurred: {str(e)}')
    
    def on_remove_roject(self):
        selected_item = self.projectsComboBox.currentText()
        self.remove_element_by_key(self.projectsJson(), selected_item)
        self.projectPath.setText('Project path')
        self.fileExtentionsTextEdit.clear()
        self.populateProjectComboBox()

    # Function to load the JSON file
    def load_json_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("The file was not found.")
            return None
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return None

    # Function to save the modified JSON back to the file
    def save_json_file(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    # Function to remove an element by key
    def remove_element_by_key(self, file_path, key_to_remove):
        # Load the existing data from the file
        data = self.load_json_file(file_path)
        
        if data is not None:
            # Check if the key exists in the data
            if key_to_remove in data:
                # Remove the element
                del data[key_to_remove]
                # Save the modified data back to the file
                self.save_json_file(file_path, data)
            else:
                print(f"Key '{key_to_remove}' not found.")
        else:
            print("Failed to load the file.")

    def get_item_by_key(self, key: str):
        with open(self.projectsJson(), "r") as file:
            try:
                # Load JSON data
                json_data = json.load(file)
                if key in json_data:
                    return json_data[key]
                else:
                    return None
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")
        
