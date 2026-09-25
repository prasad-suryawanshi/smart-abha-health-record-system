# Smart ABHA Flask — VS Code Ready

Healthcare management system (maternal & child health) built with Flask + HTML templates.

## Quick Start in VS Code

1. **Open the folder** `smart-abha-flask` in VS Code  
   (`File → Open Folder…`)

2. **Create & activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   ```

   - Windows: `venv\Scripts\activate`
   - macOS / Linux: `source venv/bin/activate`

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize sample database**

   ```bash
   python init_db.py
   ```

5. **Run the app**

   - Press **F5** and choose **Flask App**, **or**
   - Terminal: `python app.py`  
   - Or: `flask --app app run --debug`

6. Open **http://127.0.0.1:5000**

### Demo login
After `init_db.py` you can use any of the created users (password is set in the script — check `init_db.py` or use the Quick Login buttons on the login page).

## Project structure

```
smart-abha-flask/
├── .vscode/          # VS Code launch, tasks, settings
├── templates/        # Jinja2 HTML templates
├── app.py            # Flask application
├── config.py         # Configuration (defaults only — no .env required)
├── models.py         # SQLAlchemy models
├── init_db.py        # Create DB + sample data
├── requirements.txt
└── README.md
```

## Configuration

All settings have sensible defaults in `config.py` (SQLite database, development secret key, etc.).  
**No `.env` file is required.**

To change values for production, edit `config.py` or set environment variables (`SECRET_KEY`, `DATABASE_URL`, `FLASK_ENV`, …) in your shell / hosting platform.

## VS Code features included

- Debug configuration (**Flask App**)
- Tasks: Run App, Initialize Database, Lint, Format
- Recommended Python extensions
- Format-on-save (Black)

Happy coding!
