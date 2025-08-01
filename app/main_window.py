import os
import sys
import json
import time
from typing import Optional
import warnings
import subprocess
from PyQt5 import uic
from pathlib import Path
from datetime import datetime
from PyQt5.QtGui import QFont, QIntValidator, QIcon
from PyQt5.QtCore import QPoint, Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QMainWindow,
    QDesktopWidget,
    QFileDialog
)

from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

changed_files = []


class FileWalkerThread(QThread):
    # Define a signal to send file names to the main thread
    file_found = pyqtSignal(str)
    full_file_path = pyqtSignal(str)
    finished = pyqtSignal()
    processing_time = pyqtSignal(str)

    def __init__(
        self,
        directory,
        extensions,
    ):
        super().__init__()
        self.directory = Path(
            directory
        )  # Convert the directory to a pathlib.Path object
        self.extensions = extensions  # List or tuple of valid file extensions
        self.file_reader = FileReader()
        self.content = self.file_reader.get_file_content(self.resource_path(r"./database/foldersToSkip.txt"))
        self.git_status_codes = {
            "M": "Modified",
            "A": "Staged",
            "??": "Untracked",
            " ": "Untracked",
            "D": "Deleted",
            "R": "Renamed",
            "C": "Copied",
            "UU": "Conflicts.",
        }

    def run(self):
        try:
            self.start_time = time.time()
            # Walk through the directory and find files with the specified extensions
            for root, dirs, files in os.walk(self.directory):
                root_path = Path(root)
                dirs[:] = [d for d in dirs if d not in self.content]
                for file in files:
                    if file.endswith(tuple(self.extensions)):  # Check file extensions
                        full_path = root_path / file  # Construct the full file path
                        relative_path = os.path.relpath(full_path, self.directory)
                        status = subprocess.run(
                            ["git", "status", "--short", relative_path],
                            cwd=self.directory,
                            capture_output=True,
                            text=True,
                        )
                        if status.stdout.strip():  # Check if there is any output
                            self.file_found.emit(
                                f"[ {self.git_status_codes.get(status.stdout.split()[0])} ] : {relative_path}"
                            )  # Emit the full file path as a string
                            self.full_file_path.emit(str(full_path))
                        else:
                            self.file_found.emit(
                                f"[ UnModified ] : {relative_path}"
                            )  # Emit the full file path as a string

            self.finished.emit()
            self.end_time = time.time()
            self.processing_time.emit(
                f"\nTotal processing time: {self.end_time - self.start_time:.4f} seconds\n"
            )
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise e
    def resource_path(self, relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))



        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))


class PullRequestProcessor(QThread):

    # Signals to communicate with the main thread
    llm_message = pyqtSignal(str)
    process_error = pyqtSignal(str)
    process_finished = pyqtSignal(str)
    processing_time = pyqtSignal(str)

    def __init__(self, llm_model):
        super().__init__()
        self.llm_model = llm_model
        self.chain = self.prepare_llm_chain()

    def run(self):
        self.start_time = time.time()
        try:

            messages = self.get_item_by_key("messages", r"./database/dataStore.json")
            response = self.chain.invoke({"commit_messages": messages})
            message = response.get("text", "No response text found.")
            self.llm_message.emit(message)
            self.process_finished.emit("Done processing....")
            self.end_time = time.time()
            self.processing_time.emit(
                f"Total processing time: {self.end_time-self.start_time:.4f} seconds"
            )
        except Exception as e:
            self.process_error.emit(f"\nError during execution: {str(e)}\n")

    def prepare_llm_chain(self) -> LLMChain:
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        with warnings.catch_warnings():
            return LLMChain(
                llm=self.prepare_ollama_llm(),
                prompt=self.prompt_template(),
                memory=memory,
            )
    
    def prepare_ollama_llm(self) -> Optional[OllamaLLM]:
        try:
            return OllamaLLM(
                model=self.llm_model,
                temperature=0,
            )
        except Exception as e:
            print(f"Error preparing Ollama LLM: {e}")
            return None

    def prompt_template(self):
        return PromptTemplate(
            template=f"""
                        You are a highly skilled assistant specializing in creating clear, concise, and meaningful git pull request messages. 
                        Your task is to analyze the provided commit messages and any relevant prior context from the chat history to generate a cohesive and well-structured pull request description.
                        Remember not to output any of the examples as quildlines in the final response.

                        **Input Structure**:
                        - `chat_history`: A summary of prior discussions or context relevant to the changes.
                        - `commit_messages`: A list where each item is formatted as:
                        `fileName: [file name] commitMessage: [commit message]`.

                        **Requirements**:
                        - Use **past tense** for all descriptions.
                        - Ensure the pull request message is clear, descriptive, and meaningful.
                        - Group related changes or updates for improved clarity.
                        - Highlight the key contributions made in the commits.
                        - Consider context from `chat_history` to ensure accuracy and relevance.
                        - Use sections and tags (e.g., **New Feature**, **Code Refactor**, **Bug Fix**) to improve readability.
                        - Add titles or headers where necessary for better organization.

                        **Input**:
                        - `chat_history`: {{chat_history}}
                        - `commit_messages`: {{commit_messages}} 

                        **Instructions**:
                        - Parse the `commit_messages` list.
                        - Use the `chat_history` to enrich or clarify the pull request description where applicable.
                        - Synthesize the input into a cohesive pull request message that is professional, well-structured, and easy to read.

                        **Output Format**:
                        ```markdown
                        ## Pull Request Summary

                        ### New Features
                        - [Description of the new feature] for [file name(s)].
                        - [Additional details or rationale, if necessary].

                        ### Code Refactor
                        - [Description of the refactored code] for [file name(s)].
                        - [Additional details or rationale, if necessary].

                        ### Bug Fixes
                        - [Description of the bug fix] for [file name(s)].
                        - [Additional details or rationale, if necessary].

                        ### Other Changes
                        - [Grouped or miscellaneous changes].

                        **Context**
                        - [Summary of how the changes align with `chat_history`].
                        ```

                        **Example Input**:
                        ```json
                        chat_history: "Discussed adding database configurations and new API endpoints."
                        commit_messages: [
                            "fileName: ecosystem.config.js commitMessage: Added database configuration to ecosystem.config.js.",
                            "fileName: index.js commitMessage: Added API endpoints for single user GET, POST, and PUT requests.",
                            "fileName: utils.js commitMessage: Refactored utility functions to improve code readability and performance."
                        ]
                        ```

                        **Example Output**:
                        
                        ## Pull Request Summary

                        ### New Features
                        - Added database configuration for deployment in `ecosystem.config.js`.
                        - Implemented single-user API endpoints (GET, POST, and PUT) in `index.js`.

                        ### Code Refactor
                        - Refactored utility functions in `utils.js` to improve code readability and performance.

                        **Context**
                        - These changes align with previous discussions about enhancing deployment and API capabilities.
                        - Refactoring was necessary to ensure maintainability and performance improvements.
                        

                        Begin synthesizing the pull request message below:
                """,
                input_variables=["chat_history", "commit_messages"],
            )

    def get_item_by_key(self, key: str, file_name: str):
        with open(self.resource_path(file_name), "r") as file:
            try:
                # Load JSON data
                json_data = json.load(file)
                if key in json_data:
                    return json_data[key]
                else:
                    return None
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")
    
    def resource_path(self, relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))


class FileReader:
    def get_file_content(self, file_path):
        # Read file content into a list if the file exists
        if Path(file_path).exists() and Path(file_path).is_file():
            with  Path(file_path).open("r", encoding="utf-8") as file:
                content_list = [
                    line.strip() for line in file
                ]  # Stripping newline characters
            return content_list
        else:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        if getattr(sys, 'frozen', False):
            ui_path = os.path.join(sys._MEIPASS, 'views', 'main_window.ui')
        else:
            ui_path = './views/main_window.ui'  # Normal development mode
        uic.loadUi(ui_path, self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.icon = QIcon(self.resource_path("icon.ico"))
        self.setWindowIcon(self.icon)
        self.setWindowTitle("GitCommitBuddy")
        self.oldPosition = self.pos()

        self.populateComboBoxes()
        self.gitVersion.setText(self.check_git_installation())
        self.ollamaVersion.setText(self.check_ollama_installation())
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())
        self.commitMessageLenghtEdit.setValidator(QIntValidator(5, 9999))

        self.btnClose.clicked.connect(self.close_app)
        self.btnMinimize.clicked.connect(self.showMinimized)

        self.btnCommit.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.commitPage)
        )
        self.btnPullRequest.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.pullRequestPage)
        )
        #self.dialog = SettingsDialog()
        self.btnSettings.clicked.connect(self.open_dialog)
        self.btnSettings.hide()
        self.btnBrowse.clicked.connect(self.browseProjectFolder)

        self.btnRemoveProject.clicked.connect(self.on_remove_project)

        self.btnResetTextEdit.clicked.connect(self.clearContent)
        self.btnGenerateCommit.clicked.connect(self.modified_files_processor)
        self.btnGeneratePullRequest.clicked.connect(self.generate_pull_request_message)

        self.btnSaveProjectConfiguration.clicked.connect(self.saveProjectConfiguration)
        self.setFont()

        self.projectsComboBox.currentIndexChanged.connect(self.on_combo_box_changed)

    def close_app(self):
        try:
            self.close()
            #self.dialog.close()
        except Exception as e:
            print(f"{str(e)}")

    def resource_path(self, relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))

    def check_git_installation(self):
        try:
            result = subprocess.run(
                ["git", "--version"], capture_output=True, text=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return "Path to git exe not found"
        
    def check_ollama_installation(self):
        try:
            result = subprocess.run(
                ["ollama", "--version"], capture_output=True, text=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            print("Path to ollama exe not found")
            return "Path to ollama exe not found"
        
    def get_ollama_models(self):
        try:
            result = subprocess.run(
                ["ollama", "list"], capture_output=True, text=True, check=True
            )
            lines = result.stdout.strip().split('\n')

            if len(lines) < 2:
                return []

            # Skip the header and extract only the first word (model name) from each line
            model_names = [line.split()[0] for line in lines[1:] if line.strip()]
            return model_names

        except (subprocess.CalledProcessError, FileNotFoundError):
            return []

    def pull_request_error(self, message):
        self.pullTextEdit.setText(message)

    def generate_pull_request_message(self):
        try:
            self.pullTextEdit.clear()
            selected_model = self.llmModels.currentText()
            self.pullTextEdit.append(
                f"[{datetime.now()} ] Processing commit messages...\n"
            )
            if selected_model:
                self.pull_thread = PullRequestProcessor(selected_model)
                self.pull_thread.llm_message.connect(self.append_llm_pull_message)
                self.pull_thread.process_error.connect(self.pull_request_error)
                self.pull_thread.process_finished.connect(
                    self.append_llm_pull_message
                )
                self.pull_thread.processing_time.connect(
                    self.append_llm_pull_message
                )
                self.pull_thread.start()
            else:
                self.pullTextEdit.setText(
                    f"\n[{datetime.now()} ] No llm model selected...\n"
                    )
        except Exception as e:
            print(f"An error occured: {str(e)}")

    def append_llm_pull_message(self, message):
        self.pullTextEdit.append(message)

    def append_llm_message(self, message):
        self.textEdit.append(message)

    def append_processed_file(self, file_path):
        # Append the file path to the text area
        self.textEdit.append(file_path)

    def processing_finished(self):
        # Notify when the scan is complete
        self.textEdit.append("\nProcessing Completed!")

    def close_event(self, event):
        try:
            # Ensure the thread is stopped properly when closing the window
            if hasattr(self, "process_thread") or self.process_thread.isRunning():
                self.process_thread.quit()
                self.process_thread.wait()
            event.accept()
        except Exception as e:
            print(f"An error occured: {str(e)}")

    def clearContent(self):
        self.textEdit.clear()
        self.issueKeyLineEdit.clear()
        self.projectKey.clear()
        self.projectPath.setText("Project Path")
        self.fileExtentionsTextEdit.clear()
        self.commitMessageLenghtEdit.clear()

    def start_walking(self, directory, extensions):
        try:
            if directory:
                self.textEdit.append(f"Scanning directory: {directory}\n")
                # Initialize and start the file walker thread
                
                self.thread = FileWalkerThread(directory, extensions)
                self.thread.file_found.connect(self.append_file)
                self.thread.full_file_path.connect(self.get_changed_files)
                self.thread.finished.connect(self.scan_finished)
                self.thread.processing_time.connect(self.append_file)
                self.thread.start()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def append_file(self, file_path):
        # Append the file path to the text area
        self.textEdit.append(file_path)

    def get_changed_files(self, full_file_path):
        # Append the file path to the text area
        changed_files.append(full_file_path)

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
        self.dialog.set_api_key(self.get_api_key(self.resource_path(r'./database/apiKey.json')))
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
                    return data.get(
                        "apiKey", None
                    )  # Or provide a default value/message
                except json.JSONDecodeError:
                    return None  # If the file contains invalid JSON
        else:
            return None  # If the file doesn't exist or is empty

    def setFont(self):
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
        self.pullTextEdit.setFont(font1)
        self.pullTextEdit.clear()

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
        if project_name is not None and project_name != "":
            project_path = self.projectPath.text()
            file_extensions = self.fileExtentionsTextEdit.toPlainText().strip()
            self.append_to_json(
                self.resource_path(r"./database/projects.json"),
                project_name,
                project_path,
                file_extensions,
            )
            self.textEdit.append(
                f"[{datetime.now()} ] Project repository saved successfully..."
            )
            self.populateComboBoxes()
        else:
            self.textEdit.clear()
            self.textEdit.append(f"[{datetime.now()} ] Project key is required")

    def get_path_basename(self, path: str) -> str:
        return os.path.basename(path)

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
        path = self.get_json_keys(self.resource_path(r"./database/projects.json"))
        self.projectsComboBox.addItems(path)
        self.llmModels.clear()
        self.llmModels.addItems(self.get_ollama_models())

    def on_combo_box_changed(self):
        try:
            self.fileExtentionsTextEdit.clear()
            self.textEdit.clear()
            del changed_files[:]
            selected_item = self.projectsComboBox.currentText()
            item = self.get_item_by_key(selected_item, r"./database/projects.json")
            self.projectPath.setText(item["path"])
            self.projectPathPullRequest.setText(item["path"])
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
        self.remove_element_by_key(self.resource_path(r"./database/projects.json"), selected_item)
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

    def get_item_by_key(self, key: str, file_path: str):
        with open(self.resource_path(file_path), "r") as file:
            try:
                # Load JSON data
                json_data = json.load(file)
                if key in json_data:
                    return json_data[key]
                else:
                    return None
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON: {e}")

    def modified_files_processor(self):
        try:
            selected_item = self.projectsComboBox.currentText()
            selected_model = self.llmModels.currentText()

            self.fileExtentionsTextEdit.clear()
            self.textEdit.clear()
            if selected_item and selected_model:  # If the text is not empty
                self.ollama_processor()
                self.projectKey.setText(selected_item)
                self.fileExtentionsTextEdit.append(self.string_extensions)
                self.process_thread.quit()
            else:
                self.textEdit.setText(
                    f"[{datetime.now()} ] No project selected or model selected!"
                )

        except Exception as e:
            print(f"An exception occurred: {str(e)}")
    
    def ollama_processor(self):
        try:
            projectPath = self.projectPath.text()
            if len(changed_files) > 0:
                llm_model = self.llmModels.currentText()
                message_length = self.commitMessageLenghtEdit.text()
                issue_key = self.issueKeyLineEdit.text()
                toggle_tracking = self.toggleTracking.isChecked()
                self.textEdit.append(f"Processing modified files. {len(changed_files)} in total")
                self.append_llm_message(
                    "Generating commit messages, might take sometime.\n"
                )
                # Initialize and start the file walker thread
                self.process_thread = OllamaModel(
                    file_paths=changed_files,
                    llm_model=llm_model,
                    message_length=message_length or 10,
                    issue_key=issue_key,
                    is_staging_enable=toggle_tracking,
                    directory=projectPath
                )
                self.process_thread.process_file_found.connect(self.append_processed_file)

                # if self.process_thread.isRunning() == False:
                self.process_thread.process_finished.connect(self.processing_finished)
                self.process_thread.process_error.connect(self.append_processed_file)
                self.process_thread.git_installation.connect(self.append_processed_file)
                self.process_thread.llm_message.connect(self.append_llm_message)
                self.process_thread.committed.connect(self.append_llm_message)
                self.process_thread.processing_time.connect(self.append_llm_message)
                self.process_thread.start()
                # else:
                #     print("Processing is currently in progress....")
            else:
                self.textEdit.append("No modified files found...")     
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            self.process_thread.quit()


class OllamaModel(QThread):
    # Qt Signals
    process_file_found = pyqtSignal(str)
    process_finished = pyqtSignal()
    process_error = pyqtSignal(str)
    git_installation = pyqtSignal(str)
    llm_message = pyqtSignal(str)
    processing_time = pyqtSignal(str)
    committed = pyqtSignal(str)

    def __init__(self, file_paths, llm_model, message_length, issue_key, is_staging_enable,directory):
        super().__init__()
        self.llm_model = llm_model  # LLM instance is passed in
        self.message_length = message_length
        self.issue_key = issue_key
        self.is_staging_enable = is_staging_enable
        self.messages = []
        self.directory = directory
        self.chain = self.prepare_llm_chain()
        self.file_paths = [Path(p) for p in file_paths] if file_paths else []

        # Process files
    def run(self):
        self.start_time = time.time()

        # Verify the directory is a Git repository
        try:
            subprocess.run(
                ["git", "-C", self.directory, "rev-parse", "--is-inside-work-tree"],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError:
            self.process_error.emit(f"{self.directory} is not a Git repository.")
            return

        # ✅ Now use the pre-extracted file paths instead of walking the directory
        for full_path in self.file_paths:
            full_path = Path(full_path)
            relative_path = os.path.relpath(full_path, self.directory)
            relative_path = relative_path.replace('\\', '/')
            self.basename = full_path.name

            try:
                self.process_file_found.emit(
                    f"\n[{datetime.now()}] Processed: {self.basename}"
                )

                if self.is_staging_enable:
                    status = subprocess.run(
                        ["git", "status", "--short", relative_path],
                        cwd=self.directory,
                        capture_output=True,
                        text=True,
                    )
                    output = status.stdout.strip()
                    if output:
                        file_status = output[:2]
                        if file_status == "??" or file_status == " ":
                            subprocess.run(
                                ["git", "add", relative_path],
                                cwd=self.directory,
                                check=True,
                            )
                            diff_result = subprocess.run(
                                ["git", "-C", self.directory, "diff", relative_path],
                                capture_output=True,
                                text=True,
                            )
                            diff_changes = diff_result.stdout.strip()

                            if diff_result.returncode == 0 and diff_changes:
                                response = self.chain.invoke({"git_output": diff_changes})
                                generated_message = response["text"].strip().replace("\n", " ")

                                subprocess.run(
                                    ["git", "-C", self.directory, "commit", "-m", f'{self.issue_key} {generated_message}'],
                                    check=True,
                                )
                                self.process_file_found.emit(
                                    f"[{datetime.now()}] File set for tracking and committed: {self.basename} with message: {generated_message}"
                                )
                            else:
                                subprocess.run(
                                    ["git", "-C", self.directory, "commit", "-m", f"{self.issue_key} Initial commit", relative_path],
                                    check=True,
                                )
                                self.process_file_found.emit(
                                    f"[{datetime.now()}] File set for tracking with Initial commit: {self.basename}"
                                )

                result = subprocess.run(
                    ["git", "-C", self.directory, "diff", relative_path],
                    capture_output=True,
                    text=True,
                )
            
                changes = result.stdout.strip()

                if result.returncode == 0 and changes:
                    response = self.chain.invoke({"git_output": changes})
                    message = response["text"].strip().replace("\n", " ")
                    self.llm_message.emit(
                        f"[{datetime.now()}] {self.basename} Message: {self.issue_key} {message}"
                    )
                    subprocess.run(
                        ["git", "-C", self.directory, "add", relative_path],
                        check=True,
                    )
                    subprocess.run(
                        ["git", "-C", self.directory, "commit", "-m", f'{self.issue_key} {message}'],
                        check=True,
                    )
                    self.committed.emit(
                        f"[{datetime.now()}] Committed {self.basename}"
                    )
                    self.messages.append(
                        f"fileName: {self.basename} commitMessage: {message}"
                    )
                elif result.returncode != 0:
                    self.process_error.emit(
                        f"Error running git diff: {result.stderr}"
                    )
            except Exception as e:
                self.process_error.emit(f"\nAn error occurred: {str(e)}\n")

        self.update_or_append_llm_messages(self.messages)
        self.process_finished.emit()
        self.end_time = time.time()
        self.processing_time.emit(
            f"Total processing time: {self.end_time - self.start_time:.4f} seconds"
        )

    def prepare_llm_chain(self) -> LLMChain:
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        with warnings.catch_warnings():
            return LLMChain(
                llm=self.prepare_ollama_llm(),
                prompt=self.prompt_template(message_length=self.message_length),
                memory=memory,
            )
    
    def prepare_ollama_llm(self) -> Optional[OllamaLLM]:
        try:
            return OllamaLLM(
                model=self.llm_model,
                temperature=0,
            )
        except Exception as e:
            print(f"Error preparing Ollama LLM: {e}")
            return None
        
    def prompt_template(self, message_length):
        return PromptTemplate(
            template=f"""
            You are a helpful assistant that helps programmers, coders, software engineers, and developers write intuitive 
                    and concise git commit messages. The commit message should be in past tense and descriptive. Add more detail if necessary.
                    But make sure it summarizes the commit message in {message_length} words and should not include a very detailed commit message .

            ### Instructions:
            - Use past tense (e.g., "Updated...", "Added...", "Refactored...")
            - Do **not** explain your reasoning — only output the commit message.
            - **Do NOT include reasoning, thinking steps, or explanations.**
            - Do NOT use <think> or any tags.
            - If the diff is empty, return **Initial commit**
            - The message should summarize the change in **{message_length} words or fewer**.

            ### Git Diff:
            {{git_output}}

            ### Commit message:
            """,
            input_variables=["git_output"],
        )

    def update_or_append_llm_messages(self, messages):
        self.append_or_update_messages(self.resource_path(r"./database/dataStore.json"), messages)
    
    def append_or_update_messages(self, file_path: str, messages: list):
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

        # Update or add the 'apiKey'
        data["messages"] = messages

        # Write the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def resource_path(self, relative_path):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))