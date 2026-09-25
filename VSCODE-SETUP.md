# 🎯 Smart ABHA Flask - VS Code Setup Guide

Complete guide to set up and run the Smart ABHA Healthcare System in VS Code.

---

## 📋 Prerequisites

Before you start, ensure you have:
- ✅ **VS Code** installed ([download](https://code.visualstudio.com))
- ✅ **Python 3.9+** installed ([download](https://python.org))
- ✅ **Git** installed (optional but recommended)

---

## 🚀 Quick Start (3 Steps)

### **Step 1: Open Project in VS Code**

```bash
# Navigate to the project folder
cd smart-abha-flask

# Open in VS Code
code .
```

Or open VS Code → File → Open Folder → Select `smart-abha-flask`

---

### **Step 2: Install Python Extensions**

When you open the project, VS Code will prompt you to install Python extensions.

**Click "Install" when you see:**
- "We noticed a .vscode/extensions.json file..."

Or manually install these extensions:
1. **Python** - ms-python.python
2. **Pylance** - ms-python.vscode-pylance
3. **Debugpy** - ms-python.debugpy

**In VS Code:**
- Press `Ctrl+Shift+X` (Extensions)
- Search and install each extension

---

### **Step 3: Set Up Virtual Environment**

#### **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 💾 Install Dependencies

### **Option 1: Using VS Code Terminal**
1. Press `` Ctrl+` `` to open integrated terminal
2. Terminal should show `(venv)` prefix
3. Run:
```bash
pip install -r requirements.txt
```

### **Option 2: Using Task**
1. Press `Ctrl+Shift+P`
2. Type: "Run Task"
3. Select: "Install Dependencies"

---

## 🗄️ Initialize Database

### **With Sample Data:**
```bash
python init_db.py
```

**Output:**
```
🗑️  Dropping existing tables...
📁 Creating database tables...
👥 Creating demo users...
✅ Users created successfully
...
✨ DATABASE INITIALIZATION COMPLETE ✨

📊 Summary:
  👥 Users created: 4
  👩‍🤰 Maternal records: 2
  👶 Child records: 2
  💉 Vaccinations: 12
```

---

## ▶️ Run the Application

### **Option 1: Using Debug (Recommended)**
1. Press `F5` or click Run → Start Debugging
2. Choose "Flask App" configuration
3. Flask starts with full debugging support

**Features:**
- ✅ Breakpoints enabled
- ✅ Step through code
- ✅ Hot reload on file changes
- ✅ Debug console available

### **Option 2: Using Task**
1. Press `Ctrl+Shift+P`
2. Type: "Run Task"
3. Select: "Run Flask App"

### **Option 3: Manual Terminal**
```bash
python app.py
```

---

## 🌐 Access the Application

Once running, open your browser:

```
http://localhost:5000
```

**Demo Users:**
| Email | Role | Password |
|-------|------|----------|
| priya.sharma@healthcenter.com | Doctor | password123 |
| anita.asha@example.com | ASHA Worker | password123 |
| sunita.anganwadi@example.com | Anganwadi | password123 |
| admin@healthsystem.com | Admin | password123 |

---

## 🖼️ Project Structure

```
smart-abha-flask/
├── .vscode/
│   ├── launch.json          # Debug configuration
│   ├── tasks.json           # Task definitions
│   ├── settings.json        # VS Code settings
│   └── extensions.json      # Recommended extensions
├── templates/
│   ├── base.html           # Base template
│   ├── index.html          # Landing page
│   ├── login.html          # Login page
│   ├── dashboard.html      # Main dashboard
│   └── analytics.html      # Analytics dashboard
├── app.py                  # Main Flask application
├── models.py               # Database models
├── config.py               # Configuration
├── init_db.py              # Database initialization
├── requirements.txt        # Python dependencies
├──  (removed — not required)            # Environment template
└── README.md               # Documentation
```

---

## 🛠️ Common VS Code Tasks

### **Open Integrated Terminal**
- Press `` Ctrl+` ``
- Or: Terminal → New Terminal

### **Run All Tasks**
- Press `Ctrl+Shift+P`
- Type: "Run Task"
- Choose task:
  - Install Dependencies
  - Run Flask App
  - Initialize Database
  - Lint Code
  - Format Code

### **Debug with Breakpoints**
1. Click left of line number to add breakpoint (red dot)
2. Press `F5` to start debugging
3. Execution stops at breakpoint
4. Inspect variables in Debug Panel
5. Press `F10` to step over
6. Press `F11` to step into

### **Format Code**
- Right-click → Format Document
- Or: `Shift+Alt+F`

### **Search Files**
- `Ctrl+P` - Quick file search
- `Ctrl+Shift+F` - Search across project

### **Find and Replace**
- `Ctrl+H` - Open Find & Replace
- Replace in files or single file

---

## 📁 Create .env File

Create `.env` file in project root:

```bash
# Copy from template
cp  (removed — not required) .env
```

**Or create manually:**
1. Right-click in Explorer
2. New File → `.env`
3. Add content:

```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///smart_abha.db
```

---

## 🔍 Debugging Features

### **Breakpoints**
```python
# In app.py or any file
def login():
    email = request.form.get('email')  # Click left side to add breakpoint
    user = User.query.filter_by(email=email).first()
    # Execution will stop here when running in debug mode
```

### **Debug Console**
When debugging:
1. Press `F5` to start
2. Open Debug Console
3. Type Python code to inspect:
```python
> User.query.all()
> current_user.name
> db.session.query(MaternalRecord).all()
```

### **Watch Variables**
1. Click Variables in Debug Panel
2. See all local variables
3. Expand to inspect nested objects

---

## 🐛 Troubleshooting

### **Python not found**
```bash
# Check Python is installed
python --version

# Or use Python 3
python3 --version
```

### **Virtual environment not activating**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# You should see (venv) in terminal
```

### **Dependencies not installed**
```bash
pip install -r requirements.txt --upgrade
```

### **Port 5000 in use**
```bash
# Change port in launch.json or run with different port
python -c "from app import create_app; app = create_app(); app.run(port=5001)"
```

### **Database errors**
```bash
# Reinitialize database
rm smart_abha.db  # Remove old database
python init_db.py  # Create new one with sample data
```

### **Template not found**
- Ensure `templates/` folder exists
- Check template filenames match in routes
- Reload browser (Ctrl+Shift+R)

---

## 📚 VS Code Tips & Tricks

### **Multi-cursor Editing**
- `Ctrl+D` - Select next occurrence
- `Ctrl+Alt+Down` - Copy line down
- `Alt+Shift+I` - Insert cursor at end of all selected lines

### **Keyboard Shortcuts**
| Shortcut | Action |
|----------|--------|
| `Ctrl+K Ctrl+S` | Show Keyboard Shortcuts |
| `Ctrl+,` | Open Settings |
| `Ctrl+Shift+D` | Debug View |
| `Ctrl+Shift+G` | Git View |
| `Ctrl+B` | Toggle Sidebar |
| `Ctrl+J` | Toggle Terminal |

### **Source Control (Git)**
1. Press `Ctrl+Shift+G`
2. Initialize repository
3. Stage files
4. Write commit message
5. Press Commit

---

## 🌐 API Testing in VS Code

### **Option 1: REST Client Extension**
1. Install "REST Client" extension
2. Create `api.http` file:

```http
@baseUrl = http://localhost:5000

### Get maternal records
GET {{baseUrl}}/api/maternal

### Get child records
GET {{baseUrl}}/api/child

### Get analytics
GET {{baseUrl}}/api/analytics
```

3. Click "Send Request" above each request

### **Option 2: Thunder Client (Built-in)**
1. Open Extensions
2. Search "Thunder Client"
3. Install and enable
4. Open Thunder Client from Activity Bar
5. Create requests and test API

---

## 📊 Application Structure

```
REQUEST FLOW:
Browser → URL (localhost:5000/login)
  ↓
Flask Router (app.py)
  ↓
View Function (login())
  ↓
Database Query (models.py)
  ↓
Template Rendering (templates/login.html)
  ↓
HTML Response to Browser
```

---

## 🚀 Development Workflow

### **1. Make Changes**
- Edit files in VS Code
- Changes auto-reload in browser

### **2. Debug Issues**
- Set breakpoints (F5)
- Inspect variables
- Check Debug Console

### **3. Format Code**
- Press `Shift+Alt+F`
- Keep code clean and readable

### **4. Commit Changes**
- `Ctrl+Shift+G` → Git View
- Stage changes
- Write commit message

### **5. Test Application**
- Open browser to localhost:5000
- Try all user roles
- Check API endpoints

---

## 💡 Advanced Features

### **Environment Variables**
Create `.env` file for sensitive data:
```
DATABASE_URL=...
SECRET_KEY=...
API_KEY=...
```

Load in app:
```python
import os

database_url = os.getenv('DATABASE_URL')
```

### **Logging**
```python
import logging

logger = logging.getLogger(__name__)

def login():
    logger.info('Login attempt')
    # Your code
```

### **Testing**
Create `test_app.py`:
```python
import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_index(app):
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
```

Run tests:
```bash
pytest
```

---

## 🎓 Learning Resources

- **Flask Docs:** https://flask.palletsprojects.com/
- **Python Docs:** https://docs.python.org/3/
- **SQLAlchemy:** https://docs.sqlalchemy.org/
- **Jinja2:** https://jinja.palletsprojects.com/
- **VS Code Python:** https://code.visualstudio.com/docs/python/python-tutorial

---

## ✅ Checklist

- [ ] VS Code installed
- [ ] Python 3.9+ installed
- [ ] Project opened in VS Code
- [ ] Python extensions installed
- [ ] Virtual environment created
- [ ] Dependencies installed (pip install -r requirements.txt)
- [ ] Database initialized (python init_db.py)
- [ ] Application running (F5 or python app.py)
- [ ] Access http://localhost:5000 in browser
- [ ] Logged in with demo user
- [ ] Explored dashboard and features

---

## 🎉 You're Ready!

Your Smart ABHA Flask application is fully set up in VS Code and ready for development!

### Next Steps:
1. ✅ Run the app (F5)
2. ✅ Explore features in browser
3. ✅ Open files to understand code
4. ✅ Make changes and see live updates
5. ✅ Use debugger to step through code
6. ✅ Build new features!

---

**Happy Coding! 🚀**

For issues or questions, check the README.md or project documentation.
