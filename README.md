
# Streamlit Project Setup with Poetry

This project demonstrates how to set up and run a **Streamlit application** using **Poetry** as the dependency manager.

---

## Prerequisites
- Python installed (≥ 3.12 recommended)  
- Poetry installed    

---

## Step 1: Verify Installations

Check Python and Poetry versions in Command Prompt:

```bash
python --version
poetry --version
```

[!Note]
Check Poetry installation path:
```bash
where poetry
```
where poetry will give the path where poetry is installed.

Add it's path system environment variable PATH.
verify it by running below command.
```
echo %PATH%
```
## Step 2: Configure Poetry Virtual Environment
Go to the directory where you will be creating your project.

To ensure Poetry creates the virtual environment inside the project folder, run:
```bash
poetry config virtualenvs.in-project true
poetry new life_in_weeks --name project
```

## Step 3: Install Dependencies

Inside your project directory (e.g., streamlit_poc):
```bash
poetry init
poetry add streamlit
```
## Step 4: Check Virtual environment

Check if your virtual environment ```.venv``` folder is created or not. If you want to do a fresh virtual environmemt creation
you can delete ```.venv``` folder, and run below command:
```bash
poetry install
```
This will craete a fresh .venv folder

## Step 5: Run the Streamlit App

Assuming your main app file is at src/project/app.py, run:
```bash
poetry run streamlit run src/project/app.py
```
Your app will start at:
http://localhost:8501

## Step 6: Stop the Streamlit Server

If you need to stop the running app:
```powershell
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess -Force
```