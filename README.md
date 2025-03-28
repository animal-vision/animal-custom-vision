# Animal Custom Vision
- A web application for analysing animal behaviours using Azure Custom Vision.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Commit, Comment, Branch, & Pull Request Guidelines](#commit-comment-branch--pull-request-guidelines)
- [Deployment Guide](#deployment-guide-specific-to-windows)
- [Backing Up Changes](#to-backup-your-changes)
- [Acknowledgements](#acknowledgements)

## Tech Stack
- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS, Bootstrap  
- **AI/ML**: Azure Custom Vision
- **Cloud Storage**: Azure Blob Storage
- **Deployment**: Render
- **Testing**: WAVE Evaluation, Lighthouse
- **Environment**: Visual Studio Code, Python 3.13  
- **Version Control**: Git & GitHub

## Commit, Comment, Branch, & Pull Request Guidelines
- Please refer to CONTRIBUTING.md

## Deployment Guide (Specific to Windows)

### Prerequisites
Make sure you have the following installed:
- **Python 3.13+** (ensure Python is added to your system's path in environmental variables)
- **Git**
- **Visual Studio Code**
- **Azure Custom Vision** subscription

### 1. Clone the repository
Open a terminal and run:
```sh
git clone https://github.com/animal-vision/animal-custom-vision
cd animal-custom-vision
```

### 2. Create a virtual environment
```sh
python -m venv venv
```
  
### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Create `.env` file
```sh
cp .env.example .env
```

### 5. Make sure `.env` file is linked to the Azure Custom Vision model & Azure Blob Storage

### 6. Running the website
- Run **python app/app.py** in terminal
- **Ctrl + Click** on the link that appears

## To backup your changes
1. Create a new repository
2. Run in VSC terminal:
   ```sh
   git remote add backup your-backup-repo-url
   ```
3. Then (If your backup repo is added and you haven't newly cloned, just use this step):
   ```sh
   git push --mirror backup
   ```
   
## Acknowledgements
- [Stisla Bootstrap Admin Template](https://github.com/antheiz/stisla-flask)
