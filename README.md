# Animal Custom Vision

## Commit, Comment, Branch, & Pull Request Guidelines
- Please refer to CONTRIBUTING.md

## How to Run:
### 1. After cloning, run in VSC terminal (open using Ctrl + J if you have Windows):
- cp .env.example .env
- pip install -r requirements.txt

### 2. Make sure env. file is linked to the Azure Custom Vision model

### 3. Running the website
- Run **python app/app.py** in terminal
- **Ctrl + Click** on the link that appears

### To backup your changes:
1. Create a new repository
2. Run in VSC terminal: git remote add backup your-backup-repo-url
3. Then: git push --mirror backup (If your backup repo is added and you haven't newly cloned, just use this step)
