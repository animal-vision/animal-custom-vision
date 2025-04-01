# Animal Custom Vision

- A web application for analysing animal behaviours using Azure Custom Vision.

## Table of Contents

- [Team Roles](#team-roles)
- [Tech Stack](#tech-stack)
- [Commit, Comment, Branch, & Pull Request Guidelines](#commit-comment-branch--pull-request-guidelines)
- [Deployment Guide](#deployment-guide-specific-to-windows)
- [Acknowledgements](#acknowledgements)

**Documentation is available in the [`/docs`](./docs) folder.**

## Team Roles

| Name                                   | Role(s)                                |
|----------------------------------------|-----------------------------------------|
| [@sumayyah19](https://github.com/sumayyah19) | Project Leader, Product Owner           |
| [@Shelly855](https://github.com/Shelly855)       | Task Manager, Scrum Master              |
| [@JianFGO](https://github.com/JianFGO)         | Technical Lead                          |
| [@SWE-SAM](https://github.com/SWE-SAM)            | Team Member                             |
| [@zeolite-afk](https://github.com/zeolite-afk)    | Team Member                             |

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

- Ensure the `.` before `main` in `.main.routes import main` is removed (app/app.py line 5)
- Run **python app/app.py** in terminal
- **Ctrl + Click** on the link that appear

## Acknowledgements

- [Stisla Bootstrap Admin Template](https://github.com/antheiz/stisla-flask)
