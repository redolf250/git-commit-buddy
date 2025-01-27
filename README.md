# GitCommitBuddy 🧑‍💻  

GitCommitBuddy is an AI-powered assistant designed to help developers effortlessly generate meaningful and concise commit messages.  
Managing individual changes in multiple files can be overwhelming, and this tool simplifies the process by leveraging advanced large language models (LLMs).  

---

## Features 🚀  

- **AI-assisted commit messages**: Supports **Gemini-1.5-Flash-Latest** LLM from Google AI Studio and other google LLMs.  
- **Seamless file tracking**: Automatically stage/untracked files easily.  
- **Issue key tracking**: Integrate with Jira or other project management tools.  
- **Pull request summaries**: Generate clean and professional summaries with one click.  
- **Customizable settings**: Define commit message length, tracked file types, and more.  

---

## Requirements 🔧  

- A Google AI Studio API key.  
  > [Generate API Key here](https://aistudio.google.com/apikey)
- LLM from Google.  
  > [Tested with `gemini-1.5-flash-latest` 
- A Git repository initialized with a `.git` directory.  

---

## User Interface Breakdown 🖥️  

### 1. **Select LLM**  
The first dropdown lists saved LLMs from the **Settings** page.  
Choose the desired LLM to generate commit messages.  

### 2. **Select Project**  
The second dropdown lists saved projects.  
When a project is selected, the application:  
- Reads the directory contents.  
- Updates the UI to display project changes.  

The large space below displays the contents of the selected project directory.  

### 3. **Issue Key Field (Optional)**  
Enter the **issue key** for your task/bug (e.g., from Jira).  
The issue key will be appended to the commit message.  

### 4. **Message Length Box (Optional)**  
Define the maximum number of words for the commit message.  
- Default: **10** words.  
- Leave blank to use the default value.  

### 5. **Track Files Radio Button**  
Toggle this option to enable/disable automatic staging of untracked files.  

### 6. **Remove Button**  
Deletes the selected project from the database.  

### 7. **Reset Button**  
Resets the application's UI to its default state.  

### 8. **Project Path Display**  
Shows the file path of the currently selected project.  

### 9. **Project Key Field**  
Assign a unique name to a new project.  
- Default: The repository name (if unchanged).  

### 10. **New Repository Button**  
Opens a file explorer to select a Git repository folder.  
- Ensure the folder contains the `.git` directory.  
  Example:  

In this case, the `.git` folder must be inside the `app` folder.  

### 11. **File Extensions Field**  
Specify file extensions to track, separated by commas (e.g., `js,ts,json,gitignore`).  
- Save the configuration to track these file types for the selected project.  
- You can update the list later to modify tracked extensions.  

### 12. **Settings Menu**  
Opens a dialog to:  
- Save your **API Key** from the LLM provider.  
- Save new LLM models for the tool.  

---

## How It Works 🛠️  

### Adding a New Repository  
1. Click the **New Repository** button.  
2. Select a Git project folder (ensure `.git` exists in the folder).  
3. Enter file extensions to track (comma-separated).  
4. Click **Save** to save the project configuration.  

### Generating Commit Messages  
1. Select an LLM from the **Select LLM** dropdown.  
2. Choose a project from the **Select Project** dropdown.  
3. (Optional) Add an **Issue Key** and define the **Message Length**.  
4. Click the **Process** button to:  
 - Analyze changes in the tracked files.  
 - Generate meaningful commit messages.  
 - Stage the changes and commit them to the repository.  
 - Update the UI with progress details.  

### Creating a Pull Request Summary  
1. Navigate to the **Pull Request** page.  
2. Click **Generate** to create a formatted summary of the current commits.  
3. Copy and paste the summary into your pull request.  

---

## Future Enhancements 🌟  

- Support for additional LLMs from other vendors.  
- Advanced commit templates for custom workflows.  
- Enhanced pull request templates with metadata extraction.  

---

## Troubleshooting ⚙️  

- **Missing API Key**: Ensure you have a valid API key from Google AI Studio.  
- **Invalid Repository**: Make sure the selected folder is a valid Git repository.  
- **Incorrect File Extensions**: Use comma-separated values without spaces.  
Example: `js,ts,css,json`.  
- For unexpected errors, use the **Reset** button to restore the default UI.  

---

## Screenshots 📸  

### Homepage and commits generating page
![Commits Page](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/home.png)

### Sample commits made by the assistant
![Sample Commits](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/samplecommits.png)

### Pull request generating page
![Sample Commits](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/pullpage.png)

### Sample pull request content based on the commits made by the assistant
![Sample Commits](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/pullmesage.png)

### Sample pull request content rendered on GitHub 
![Sample Commits](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/gitpull.png)

### Setting page
![Sample Commits](https://github.com/redolf250/git-commit-buddy/blob/dev/redolf/images/settings.png)
---

### Contributions 🤝  

We welcome contributions! Feel free to open issues or submit pull requests.  

---

### License 📝  

This project is licensed under the MIT License.  

