# 🚀 Smart ABHA Flask - Complete Getting Started Guide

**Complete step-by-step guide to set up, run, and use the Smart ABHA Flask Healthcare System.**

---

## ⏱️ Timeline

- **5 minutes:** Run the application
- **15 minutes:** Explore all features
- **30 minutes:** Understand the code
- **1 hour:** Customize and extend

---

## ✅ Prerequisites Checklist

Before starting, verify you have:

- [ ] **Python 3.9+** - Check with `python --version`
- [ ] **Pip package manager** - Check with `pip --version`
- [ ] **VS Code** (optional) - [Download](https://code.visualstudio.com)
- [ ] **Git** (optional) - [Download](https://git-scm.com)

---

## 🎯 Step 1: Setup Project (2 minutes)

### **1.1 Download/Extract Project**

```bash
# Option A: Clone from Git
git clone https://github.com/your-repo/smart-abha-flask.git
cd smart-abha-flask

# Option B: Extract ZIP file
# Extract smart-abha-flask.zip
# Open terminal/command prompt
# cd smart-abha-flask
```

### **1.2 Verify Project Structure**

You should see:
```
smart-abha-flask/
├── app.py
├── models.py
├── config.py
├── init_db.py
├── requirements.txt
├── templates/
└── README-FLASK.md
```

---

## 🐍 Step 2: Create Python Environment (2 minutes)

### **Windows:**
```bash
python -m venv venv
venv\Scripts\activate

# You should see (venv) in your prompt
```

### **macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

# You should see (venv) in your prompt
```

---

## 📦 Step 3: Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

**Output should show:**
```
Successfully installed flask-2.3.3 flask-sqlalchemy-3.0.5 ...
```

---

## 🗄️ Step 4: Initialize Database (1 minute)

```bash
python init_db.py
```

**Expected output:**
```
✨ DATABASE INITIALIZATION COMPLETE ✨

📊 Summary:
  👥 Users created: 4
  👩‍🤰 Maternal records: 2
  👶 Child records: 2
  💉 Vaccinations: 12
  📈 Growth metrics: 2
  🔔 Reminders: 4
```

---

## ▶️ Step 5: Run the Application (1 minute)

### **Option 1: Direct Python**
```bash
python app.py
```

### **Option 2: Using Flask CLI**
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# On Windows:
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

### **Option 3: VS Code (with F5)**
1. Press `F5`
2. Select "Flask App"
3. Click Start Debugging

**Success message:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## 🌐 Step 6: Open in Browser (30 seconds)

Open your web browser and navigate to:

```
http://localhost:5000
```

You should see the **Smart ABHA landing page** 🎉

---

## 👤 Step 7: Login with Demo Users (1 minute)

### **Option A: Quick Login (Recommended)**
1. Click "Login to System"
2. See demo users listed
3. Click on any user to instantly login (no password)

### **Option B: Manual Login**
1. Click "Login to System"
2. Enter email: `priya.sharma@healthcenter.com`
3. Enter password: `password123`
4. Click "Login"

**Demo Users:**
| Name | Email | Role |
|------|-------|------|
| Dr. Priya Sharma | priya.sharma@healthcenter.com | Doctor |
| Anita Kumar | anita.asha@example.com | ASHA Worker |
| Sunita Patel | sunita.anganwadi@example.com | Anganwadi Worker |
| Rajesh Kumar | admin@healthsystem.com | Admin |

---

## 🎮 Step 8: Explore Features (10 minutes)

### **8.1 Dashboard**
- See system statistics (maternal records, child records)
- View pending reminders
- Browse maternal and child records
- Click "View Analytics" button

### **8.2 Maternal Records**
- Click any maternal record card
- View pregnancy details
- See checkup history
- Review blood tests and ultrasounds
- Click "Download Report" to export

### **8.3 Child Records**
- Click any child record card
- View vaccination schedule
- Check growth metrics
- See health checkups
- Review follow-up dates

### **8.4 Analytics Dashboard**
- Click "📊 View Analytics" button
- See system-wide statistics
- View vaccination coverage
- Check growth trends
- Download reports (CSV/JSON/Text)

### **8.5 Try Different Roles**
1. Click "Logout" (top right)
2. Login with different user
3. Notice dashboard changes based on role

---

## 📝 Step 9: Explore the Code (20 minutes)

### **9.1 Main Files Overview**

**app.py** (Main Application - 600+ lines)
```python
# Routes defined here:
@app.route('/')              # Landing page
@app.route('/login')         # Login
@app.route('/dashboard')     # Dashboard
@app.route('/analytics')     # Analytics
@app.route('/maternal')      # Maternal records
@app.route('/child')         # Child records
@app.route('/api/maternal')  # API endpoints
```

**models.py** (Database Models - 400+ lines)
```python
# Database tables:
- User (authentication)
- MaternalRecord (maternal health)
- ChildRecord (child health)
- Checkup (medical checkups)
- Vaccination (immunization)
- GrowthMetric (child growth)
- Reminder (follow-ups)
```

**config.py** (Configuration - 50+ lines)
```python
# Settings:
- Database URL
- Secret key
- Debug mode
- Session settings
```

### **9.2 Open in VS Code**
```bash
code .
```

### **9.3 Read Code Structures**
1. Open `app.py`
2. Find route definitions (starting with `@app.route`)
3. See how requests are handled
4. Check template rendering

---

## 🎨 Step 10: Customize Application (15 minutes)

### **10.1 Change App Name**

**In templates/base.html** (around line 50):
```html
<!-- Change from: -->
<a href="{{ url_for('index') }}" class="brand">🏥 Smart ABHA</a>

<!-- To: -->
<a href="{{ url_for('index') }}" class="brand">🏥 My Health System</a>
```

### **10.2 Change Colors**

**In templates/base.html** (around line 12):
```css
:root {
    --primary: #1e40af;        /* Change this blue */
    --secondary: #0891b2;      /* Change this cyan */
    --accent: #ec4899;         /* Change this pink */
    --success: #16a34a;        /* Change this green */
}
```

### **10.3 Modify Sample Data**

**Edit init_db.py** (around line 50):
```python
users = [
    User(
        name='Your Doctor Name',        # Change this
        email='your@email.com',         # Change this
        role=UserRole.DOCTOR,
    ),
    # ... add more users
]
```

### **10.4 Add New User**
```python
# In init_db.py, add to users list:
User(
    name='Dr. Your Name',
    email='your.name@example.com',
    role=UserRole.DOCTOR,
    active=True
)
```

Then reinitialize:
```bash
python init_db.py
```

---

## 🔍 Step 11: Test Features (10 minutes)

### **11.1 Create New Records**
1. Go to Dashboard
2. Click "+ New Maternal Record"
3. Fill in details
4. Click Submit
5. See record appear in list

### **11.2 View Analytics**
1. Click "📊 View Analytics"
2. See all statistics
3. Check vaccination coverage
4. Review growth trends

### **11.3 Export Reports**
1. Go to any record
2. Click "Export Report"
3. Choose format (CSV/JSON/Text)
4. Download automatically

### **11.4 Test API Endpoints**

**Open terminal/PowerShell:**

```bash
# Get maternal records
curl http://localhost:5000/api/maternal

# Get child records
curl http://localhost:5000/api/child

# Get analytics
curl http://localhost:5000/api/analytics
```

---

## 📁 Step 12: Folder Structure Explained

```
smart-abha-flask/
│
├── 📄 app.py
│   └─ Main Flask application
│      Routes, views, API endpoints
│
├── 📄 models.py
│   └─ Database tables/models
│      User, MaternalRecord, ChildRecord, etc.
│
├── 📄 config.py
│   └─ Configuration settings
│      Database URL, debug mode, etc.
│
├── 📄 init_db.py
│   └─ Database initialization
│      Create tables, add sample data
│
├── 📁 templates/
│   ├─ base.html          (Layout & styling)
│   ├─ index.html         (Landing page)
│   ├─ login.html         (Login page)
│   ├─ dashboard.html     (Main dashboard)
│   ├─ analytics.html     (Analytics dashboard)
│   ├─ maternal_list.html (Maternal records)
│   ├─ maternal_detail.html (Maternal detail)
│   ├─ child_list.html    (Child records)
│   ├─ child_detail.html  (Child detail)
│   └─ More...
│
├── 📁 .vscode/
│   ├─ launch.json       (Debug settings)
│   ├─ tasks.json        (Task definitions)
│   ├─ settings.json     (VS Code settings)
│   └─ extensions.json   (Recommended extensions)
│
├── 📄 requirements.txt
│   └─ Python dependencies
│
├── 📄 README-FLASK.md
│   └─ Complete documentation
│
└── 📄 VSCODE-SETUP.md
    └─ VS Code setup guide
```

---

## 🛠️ Common Tasks

### **Stop the Application**
Press `Ctrl+C` in terminal

### **Restart the Application**
```bash
# After making changes:
python app.py
```

### **Clear Database**
```bash
rm smart_abha.db      # Linux/macOS
del smart_abha.db     # Windows (PowerShell)
python init_db.py     # Reinitialize
```

### **Update Dependencies**
```bash
pip install --upgrade -r requirements.txt
```

---

## 🐛 Troubleshooting

### **"Python not found"**
```bash
# Install Python from python.org
# Then use:
python3 --version
python3 app.py
```

### **"Port 5000 in use"**
```bash
# Use different port:
python -c "from app import create_app; app = create_app(); app.run(port=5001)"
```

### **"ModuleNotFoundError"**
```bash
# Reinstall dependencies:
pip install --upgrade -r requirements.txt
```

### **"Template not found"**
1. Check `templates/` folder exists
2. Check template filename is correct
3. Restart Flask app
4. Hard refresh browser (Ctrl+Shift+R)

### **Database locked error**
```bash
# Remove and recreate database:
rm smart_abha.db
python init_db.py
```

---

## 📚 Files to Read

1. **README-FLASK.md** - Complete documentation
2. **VSCODE-SETUP.md** - VS Code setup guide
3. **app.py** - Main application (has comments)
4. **models.py** - Database structure
5. **templates/base.html** - Styling and layout

---

## 🎓 What You Learned

✅ How to set up Python Flask project  
✅ How to create and manage database  
✅ How to run a web application  
✅ How to login and explore features  
✅ How to understand project structure  
✅ How to customize the application  
✅ How to test features and APIs  

---

## 🚀 What's Next

### **To Learn More:**
1. Read README-FLASK.md for complete documentation
2. Explore app.py to understand routing
3. Check models.py for database structure
4. Modify templates/ to customize UI

### **To Add Features:**
1. Create new routes in app.py
2. Add database models in models.py
3. Create HTML templates in templates/
4. Test new features in browser

### **To Deploy:**
1. See deployment guides in documentation
2. Options: Heroku, AWS, DigitalOcean, etc.
3. Set up production database (PostgreSQL)
4. Configure security settings

---

## ✅ Complete Checklist

- [ ] Python 3.9+ installed
- [ ] Project downloaded/cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Database initialized
- [ ] Application running
- [ ] Accessed http://localhost:5000
- [ ] Logged in with demo user
- [ ] Explored dashboard
- [ ] Checked analytics
- [ ] Downloaded a report
- [ ] Reviewed code structure

---

## 🎉 Congratulations!

You now have a **fully functional healthcare management system** running locally! 

### Your system includes:
✅ User authentication  
✅ Maternal health tracking  
✅ Child health records  
✅ Vaccination management  
✅ Growth monitoring  
✅ Analytics dashboard  
✅ Report export  
✅ API endpoints  

---

## 🌟 Pro Tips

1. **Use VS Code for better development experience**
   - Press F5 to debug
   - Set breakpoints to inspect code
   - Use integrated terminal

2. **Hot reload is enabled**
   - Change HTML/CSS = instant update
   - Change Python = auto-restart (if configured)

3. **Use browser DevTools (F12)**
   - Check Console for errors
   - Use Network tab to see API calls
   - Inspect HTML elements

4. **Secrets can be set via environment variables or config.py**
   - Never commit to Git
   - Use for sensitive settings
   - Different values for dev/prod

---

## 📞 Need Help?

1. **Check Documentation**
   - README-FLASK.md
   - VSCODE-SETUP.md

2. **Read Code Comments**
   - app.py has detailed comments
   - models.py explains each table

3. **Search Online**
   - Flask documentation
   - Python documentation
   - Stack Overflow

4. **Check Troubleshooting Section**
   - Common issues listed
   - Solutions provided

---

## 🚀 Ready to Build?

Your Smart ABHA Flask healthcare system is ready!

### Start your journey:
```bash
# 1. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 2. Run application
python app.py

# 3. Open browser
# http://localhost:5000

# 4. Explore and build!
```

---

**Happy Coding! 🎉**

Your healthcare management system awaits! 🏥💻

Built with ❤️ for better healthcare delivery 🇮🇳
