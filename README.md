# PDF_Analyzer

An application for reading and analyzing specific aspects of PDF files.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python 3.8+](https://www.python.org/downloads/)
* [Visual Studio Code](https://code.visualstudio.com/) (Recommended IDE)

### Local Development Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/GRCosta/PDF_Analyzer.git](https://github.com/GRCosta/PDF_Analyzer.git)
    cd PDF_Analyzer
    ```

2.  **Create and activate a Virtual Environment:**
    A virtual environment isolates this project's dependencies.

    * **Create:**
        ```bash
        python -m venv .venv
        ```
    * **Activate (macOS/Linux):**
        ```bash
        source .venv/bin/activate
        ```
    * **Activate (Windows - Command Prompt):**
        ```bash
        .venv\Scripts\activate.bat
        ```

3.  **Configure VS Code:**
    Open the command palette (Ctrl+Shift+P) and select **Python: Select Interpreter**, choosing the path within the newly created `.venv` folder.

    ... (Previous content remains the same)

4.  **Install Dependencies:**
    With the virtual environment activated, install the required packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Running the Application (Future Step):**
    Once the core application code is written, you will be able to run it using the main script:
    ```bash
    python main.py  # Assuming your main script is named main.py
    ```

## ⚙️ Initial Project Structure and Git

Now is a good time to create a minimal project structure and prepare for your first commit.

### 1. Create Initial Files

Create the following files in your `PDF_Analyzer` directory:

* `main.py`: This will be the main entry point for your application.
* `.gitignore`: This crucial file tells Git which files and folders to **ignore** (like the large, auto-generated `.venv` folder).

### 2. Configure `.gitignore`

Add the following content to your `.gitignore` file. This is standard for Python projects and prevents your repository from getting bloated with unnecessary files:

```gitignore
# Virtual environment
.venv/
venv/
env/

# Byte-compiled files
__pycache__/
*.pyc
*.pyo

# Editor/OS temporary files
.vscode/
.DS_Store