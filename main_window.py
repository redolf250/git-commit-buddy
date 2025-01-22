import os
import json
from PyQt5 import uic
from pathlib import Path
from datetime import datetime
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QPoint, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QMainWindow,
    QDesktopWidget,
    QFileDialog,
    QDialog,
    QGraphicsDropShadowEffect,
)


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/api_key_dialog.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowModality(Qt.ApplicationModal)
        self.btnClose.clicked.connect(self.close)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(230, 230, 230, 50))
        self.setGraphicsEffect(self.shadow)
        self.mouseMoveEvent = self.MoveWindow

        self.btnSaveKey.clicked.connect(self.update_api_key)
        self.btnSaveModel.clicked.connect(self.update_or_append_llm_model)

    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def set_api_key(self, text):
        self.apiKeyEdit.setText(text)

    def update_api_key(self):
        key = self.apiKeyEdit.text()
        self.append_or_update_api_key(self.get_json_path("apiKey.json"), key)
        self.keyStatus.setText(f"Key updated: {datetime.now()}")

    def update_or_append_llm_model(self):
        model_name = self.llmModelName.text()
        self.append_or_update_llm_model(self.get_json_path("llmModels.json"), model_name)
        self.keyStatus.setText(f"Model inserted or updated successfully.\n{datetime.now()}")
    
    def get_json_path(self, file_name: str):
        # Determine root directory based on OS
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        json_path = Path(root_dir) / f"{file_name}"
        return json_path

    def append_or_update_api_key(self, file_path: str, api_key: str):
        """
        Append or update the 'apiKey' entry in a JSON file.
        If the file doesn't exist or is empty, create it with the 'apiKey'.
        If the 'apiKey' already exists, update its value.
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
            data = {}  # Initialize as an empty dictionary if file doesn't exist or is empty

        # Update or add the 'apiKey'
        data["apiKey"] = api_key

        # Write the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def append_or_update_llm_model(self, file_path: str, model_name: str):
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
            data = {}  # Initialize as an empty dictionary if file doesn't exist or is empty

        # Update or add the 'apiKey'
        data[f"{model_name}"] = model_name

        # Write the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)


class FileWalkerThread(QThread):
    # Define a signal to send file names to the main thread
    file_found = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, directory, extensions):
        super().__init__()
        self.directory = Path(
            directory
        )  # Convert the directory to a pathlib.Path object
        self.extensions = extensions  # List or tuple of valid file extensions

    def run(self):
        # Walk through the directory and find files with the specified extensions
        for root, _, files in os.walk(self.directory):
            root_path = Path(root)  # Convert the root to a pathlib.Path object
            for file in files:
                if file.endswith(tuple(self.extensions)):  # Check file extensions
                    full_path = root_path / file  # Construct the full file path
                    self.file_found.emit(
                        str(full_path)
                    )  # Emit the full file path as a string
                    print(os.path.basename(full_path))
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main_window.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        self.create_program_directory()
        self.populateComboBoxes()
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())
        self.dialog = SettingsDialog()

        self.btnClose.clicked.connect(self.close_app)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btnCommit.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.commitPage)
        )
        self.btnPullRequest.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pullRequestPage)
        )
        self.btnSettings.clicked.connect(self.open_dialog)

        self.btnBrowse.clicked.connect(self.browseProjectFolder)

        self.btnRemoveProject.clicked.connect(self.on_remove_project)

        self.btnResetTextEdit.clicked.connect(self.clearContent)

        self.btnSaveProjectConfiguration.clicked.connect(self.saveProjectConfiguration)
        self.setExtentionsFont()

        self.projectsComboBox.currentIndexChanged.connect(self.on_combo_box_changed)

    def close_app(self):
        try:
            self.close()
            self.dialog.close()
        except Exception as e:
            print(f"{str(e)}")
    
    def apiKeyPath(self):
        # Determine root directory based on OS
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        json_path = Path(root_dir) / "apiKey.json"
        return json_path

    def clearContent(self):
        self.textEdit.clear()
        self.issueKeyLineEdit.clear()
        self.projectKey.clear()
        self.projectPath.setText('Project Path')
        self.fileExtentionsTextEdit.clear()
        self.commitMessageLenghtEdit.clear()

    def start_walking(self, directory, extensions):
        try:
            if directory:
                self.textEdit.append(f"Scanning directory: {directory}\n")
                # Initialize and start the file walker thread
                self.thread = FileWalkerThread(directory, extensions)
                self.thread.file_found.connect(self.append_file)
                self.thread.finished.connect(self.scan_finished)
                self.thread.start()
        except Exception as e:
            print(f"An error occured: {str(e)}")

    def append_file(self, file_path):
        # Append the file path to the text area
        self.textEdit.append(file_path)

    def scan_finished(self):
        # Notify when the scan is complete
        self.textEdit.append("\nScan Complete!")

    def closeEvent(self, event):
        try:
            # Ensure the thread is stopped properly when closing the window
            if hasattr(self, "thread") and self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()
            event.accept()
        except Exception as e:
            print(f"An error occured: {str(e)}")

    def open_dialog(self):
        self.dialog.set_api_key(self.get_api_key(self.apiKeyPath()))
        self.dialog.show()

    def get_api_key(self, file_path: str):
        """
        Read the JSON file and return the value of the 'apiKey' entry.
        If the key does not exist, return None or a custom message.
        """
        # Check if the file exists and is not empty
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            # Load existing JSON data
            with open(file_path, "r") as file:
                try:
                    data = json.load(file)
                    # Return the value of 'apiKey' if it exists, else return None
                    return data.get("apiKey", None)  # Or provide a default value/message
                except json.JSONDecodeError:
                    return None  # If the file contains invalid JSON
        else:
            return None  # If the file doesn't exist or is empty

    def setExtentionsFont(self):
        font = QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(15)  # Set font size to 14
        self.fileExtentionsTextEdit.setFont(font)
        self.fileExtentionsTextEdit.clear()
        font1 = QFont()
        # font1.setFamily('Baskerville Old Face')
        font1.setPointSize(11)
        self.textEdit.setFont(font1)
        self.textEdit.clear()

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
            self.get_json_path("projects.json"), project_name, project_path, file_extensions
        )
        self.populateComboBoxes()

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
            json_models = os.path.join(root_dir, "llmModels.json")
            json_models = Path(json_models)
            json_models.touch(exist_ok=True)

    def get_json_path(self, file_name: str):
        # Determine root directory based on OS
        if os.name == "nt":  # For Windows
            root_dir = os.path.join("C:", "ProgramData", "GitCommitBuddy")
        else:  # For Unix-based systems (Linux/macOS)
            root_dir = os.path.join(os.sep, "ProgramData", "GitCommitBuddy")
        json_path = Path(root_dir) / f"{file_name}"
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

    def populateComboBoxes(self):
        self.projectsComboBox.clear()
        path = self.get_json_keys(self.get_json_path("projects.json"))
        self.projectsComboBox.addItems(path)
        self.llmModels.clear()
        path = self.get_json_keys(self.get_json_path("llmModels.json"))
        self.llmModels.addItems(path)

    def on_combo_box_changed(self):
        try:
            self.fileExtentionsTextEdit.clear()
            self.textEdit.clear()
            selected_item = self.projectsComboBox.currentText()
            item = self.get_item_by_key(selected_item, "projects.json")
            self.projectPath.setText(item["path"])
            self.string_extensions = item["extensions"]
            self.start_walking(
                item["path"], [ext.strip() for ext in self.string_extensions.split(",")]
            )
            self.projectKey.setText(selected_item)
            self.fileExtentionsTextEdit.append(self.string_extensions)
        except Exception as e:
            print(f"An exception occurred: {str(e)}")

    def on_remove_project(self):
        selected_item = self.projectsComboBox.currentText()
        self.remove_element_by_key(self.get_json_path("projects.json"), selected_item)
        self.projectPath.setText("Project path")
        self.fileExtentionsTextEdit.clear()
        self.populateComboBoxes()

    # Function to load the JSON file
    def load_json_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("The file was not found.")
            return None
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return None

    # Function to save the modified JSON back to the file
    def save_json_file(self, file_path, data):
        with open(file_path, "w") as file:
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

    def get_item_by_key(self, key: str, file_name: str):
        with open(self.get_json_path(file_name), "r") as file:
            try:
                # Load JSON data
                json_data = json.load(file)
                if key in json_data:
                    return json_data[key]
                else:
                    return None
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")
