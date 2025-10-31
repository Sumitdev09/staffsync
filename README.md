# 🚀 StaffSync - Modern Employee Management System

<div align="center">

![StaffSync Logo](https://img.shields.io/badge/StaffSync-Employee%20Management-blue?style=for-the-badge&logo=users)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg?style=flat&logo=flask)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-orange.svg?style=flat&logo=sqlite)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](LICENSE)

**A comprehensive, modern web-based employee management system built with Flask**

[🎯 Live Preview](#-live-preview--how-to-run) • [✨ Features](#-features) • [🚀 Quick Start](#-quick-start) • [📖 Documentation](#-documentation)

</div>

---

## 🌐 Live Preview & How to Run

### **⚡ Quick Start (2 minutes)**

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Sumitdev09/staffsync.git
cd staffsync

# 2️⃣ Automated setup (Linux/macOS)
chmod +x setup.sh && ./setup.sh

# For Windows: run setup.bat instead

# 3️⃣ Start the application
python run.py
```

### **🔗 Access Live Preview**

Once running, open your browser and go to:

| **Access Point** | **URL** | **Purpose** |
|------------------|---------|-------------|
| 🏠 **Main Application** | [http://localhost:5000](http://localhost:5000) | Login page |
| 👑 **Admin Dashboard** | [http://localhost:5000/admin/dashboard](http://localhost:5000/admin/dashboard) | Admin panel |
| 👤 **Staff Portal** | [http://localhost:5000/staff/dashboard](http://localhost:5000/staff/dashboard) | Employee portal |

### **🔐 Test Login Credentials**

| **Role** | **Username** | **Password** | **Access Level** |
|----------|--------------|--------------|------------------|
| 👑 Admin | `admin` | `admin123` | Full system access |
| 👤 Staff | `john.doe` | `pass123` | Employee functions |
| 👤 Staff | `jane.smith` | `pass123` | Employee functions |

### **📱 Features to Test**

✅ **Admin Panel**: Employee management, payroll processing, attendance tracking  
✅ **Staff Portal**: Personal dashboard, profile management, leave requests  
✅ **Responsive Design**: Test on desktop, tablet, and mobile  
✅ **Real-time Updates**: Live notifications and data synchronization  

### **🔧 Quick Troubleshooting**

| **Issue** | **Solution** |
|-----------|--------------|
| Port 5000 in use | `lsof -ti:5000 \| xargs kill -9` then restart |
| Python not found | Install Python 3.8+ from [python.org](https://python.org) |
| Dependencies error | Run `pip install -r requirements.txt` |
| Database error | Run `python -c "from src.app import init_database; init_database()"` |

> 💡 **Tip**: For development, use `FLASK_DEBUG=True python run.py` for auto-reload

---

---

## 📋 Table of Contents

- [🌟 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📋 Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Installation Guide](#️-installation-guide)
- [🔧 Configuration](#-configuration)
- [💻 Usage](#-usage)
- [🏗️ Project Structure](#️-project-structure)
- [🎨 Screenshots](#-screenshots)
- [📖 API Documentation](#-api-documentation)
- [🧪 Testing](#-testing)
- [🚢 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🆘 Support](#-support)

---

## 🌟 Overview

**StaffSync** is a modern, comprehensive employee management system designed to streamline HR operations and enhance workforce productivity. Built with Flask and featuring a beautiful, responsive interface, StaffSync provides all the tools needed to manage employees, attendance, payroll, and departments efficiently.

### 🎯 Why StaffSync?

- **🎨 Modern UI/UX**: Clean, professional interface with glass morphism design
- **📱 Fully Responsive**: Works perfectly on desktop, tablet, and mobile devices  
- **🔐 Secure**: Built-in authentication with role-based access control
- **⚡ Fast & Lightweight**: Optimized performance with SQLite database
- **🛡️ Production Ready**: Comprehensive error handling and security features
- **🔧 Highly Configurable**: Easy to customize and extend

---

## ✨ Features

### 👑 **Admin Dashboard**
- **📊 Real-time Analytics**: Employee statistics, attendance metrics, payroll summaries
- **📈 Interactive Charts**: Visual data representation with Chart.js
- **🚨 Notifications**: System alerts and important updates
- **⚙️ System Management**: Comprehensive administrative controls

### 👥 **Employee Management**
- **➕ Add/Edit Employees**: Complete employee profile management
- **🔍 Advanced Search & Filter**: Find employees by department, position, or status
- **📁 Department Organization**: Structured departmental hierarchy
- **💼 Position Management**: Role and responsibility tracking
- **📊 Employee Analytics**: Individual performance metrics

### 📋 **Attendance Tracking**
- **⏰ Real-time Clock In/Out**: Easy attendance marking
- **📅 Monthly/Weekly Views**: Comprehensive attendance calendars
- **📊 Attendance Reports**: Detailed attendance analytics
- **🚫 Leave Management**: Leave requests and approval system
- **📈 Attendance Trends**: Visual attendance patterns

### 💰 **Payroll Management**
- **💵 Salary Processing**: Automated payroll calculations
- **📊 Pay Period Management**: Flexible pay period configurations
- **💸 Allowances & Deductions**: Comprehensive salary components
- **📄 Payslip Generation**: Professional payslip downloads
- **📈 Payroll Reports**: Detailed financial reporting

### 🏢 **Department Management**
- **🏗️ Department Structure**: Hierarchical organization setup
- **👥 Team Management**: Department-wise employee allocation
- **📊 Department Analytics**: Performance metrics by department
- **⚙️ Department Settings**: Customizable department configurations

### 👤 **Staff Portal**
- **📊 Personal Dashboard**: Individual employee interface
- **👤 Profile Management**: Self-service profile updates
- **📅 Attendance View**: Personal attendance tracking
- **🏖️ Leave Requests**: Easy leave application system
- **💰 Payroll Access**: Personal payroll information

---

## 🛠️ Tech Stack

### **Backend**
- **🐍 Python 3.8+**: Core programming language
- **🌶️ Flask 2.3+**: Lightweight web framework
- **🗄️ SQLite**: Database management
- **🔐 Werkzeug**: Password hashing and security
- **📅 DateTime**: Date and time handling

### **Frontend**
- **🎨 HTML5 & CSS3**: Modern markup and styling
- **⚡ JavaScript (ES6+)**: Interactive functionality
- **📊 Chart.js**: Data visualization
- **🎪 Font Awesome**: Icon library
- **🌈 CSS Variables**: Theming system

### **Design System**
- **🔮 Glass Morphism**: Modern UI design trend
- **📱 Responsive Design**: Mobile-first approach  
- **🎨 CSS Grid & Flexbox**: Advanced layouts
- **✨ Smooth Animations**: Enhanced user experience

---

## 📋 Prerequisites

Before installing StaffSync, ensure you have the following installed on your system:

### **Required Software**
- **Python 3.8 or higher** ([Download Python](https://python.org/downloads/))
- **pip** (Python package manager - included with Python)
- **Git** (for cloning the repository)

### **Operating System Support**
- ✅ **Windows** 10/11
- ✅ **macOS** 10.14+
- ✅ **Linux** (Ubuntu 18.04+, CentOS 7+, etc.)

### **Hardware Requirements**
- **RAM**: 512MB minimum (2GB recommended)
- **Storage**: 100MB free space
- **Network**: Internet connection for initial setup

---

## 🚀 Quick Start

Get StaffSync running in less than 5 minutes!

### **Method 1: Automated Setup (Recommended)**

```bash
# 1. Clone the repository
git clone https://github.com/Sumitdev09/staffsync.git
cd staffsync

# 2. Run automated setup
# For Linux/macOS:
chmod +x setup.sh
./setup.sh

# For Windows:
setup.bat

# 3. Run the application
python run.py
```

### **Method 2: Manual Setup**

```bash
# 1. Clone and navigate
git clone https://github.com/Sumitdev09/staffsync.git
cd staffsync

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python run.py
```

### **🌐 Access the Application**

Once running, open your browser and navigate to:
- **Main Application**: [http://localhost:5000](http://localhost:5000)
- **Admin Panel**: [http://localhost:5000/admin/dashboard](http://localhost:5000/admin/dashboard)
- **Staff Portal**: [http://localhost:5000/staff/dashboard](http://localhost:5000/staff/dashboard)

### **🔐 Default Login Credentials**

| Role  | Username    | Password |
|-------|-------------|----------|
| Admin | `admin`     | `admin123` |
| Staff | `john.doe`  | `pass123` |
| Staff | `jane.smith`| `pass123` |
| Staff | `mike.johnson`| `pass123` |
| Staff | `sarah.wilson`| `pass123` |
| Staff | `david.brown`| `pass123` |

> ⚠️ **Security Note**: Change default passwords immediately in production!

---

## ⚙️ Installation Guide

### **Step 1: System Requirements Check**

```bash
# Check Python version (must be 3.8+)
python --version
# or
python3 --version

# Check pip installation
pip --version
# or
pip3 --version
```

### **Step 2: Clone Repository**

```bash
# Using HTTPS
git clone https://github.com/Sumitdev09/staffsync.git

# Using SSH (if configured)
git clone git@github.com:Sumitdev09/staffsync.git

# Navigate to directory
cd staffsync
```

### **Step 3: Environment Setup**

#### **Option A: Automatic Setup**
```bash
# Linux/macOS
./setup.sh

# Windows
setup.bat
```

#### **Option B: Manual Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Linux/macOS:
source venv/bin/activate
# Windows Command Prompt:
venv\Scripts\activate
# Windows PowerShell:
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### **Step 4: Database Initialization**

The database is automatically initialized on first run, but you can also manually initialize:

```bash
# Run the application (database auto-initializes)
python run.py
```

### **Step 5: Verification**

```bash
# Test the installation
curl http://localhost:5000
# or open http://localhost:5000 in your browser
```

---

## 🔧 Configuration

### **Environment Variables**

Create a `.env` file in the project root for custom configuration:

```bash
# .env file
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
SECRET_KEY=your-super-secret-key-here
```

### **Configuration Files**

#### **src/config/config.py**
```python
# Development configuration
DEBUG = True
SECRET_KEY = 'development-key'

# Production configuration  
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
```

### **Database Configuration**

StaffSync uses SQLite by default. For production, you can modify the database configuration:

```python
# In src/config/config.py
DATABASE_PATH = 'production_staffsync.db'
```

---

## 💻 Usage

### **Admin Functions**

#### **Employee Management**
1. **Navigate to Admin Panel**: Login as admin → Admin Dashboard
2. **Add Employee**: Employees → Add Employee Button
3. **Edit Employee**: Click Edit icon in employee row  
4. **Delete Employee**: Click Delete icon (with confirmation)

#### **Payroll Management**
1. **Generate Payroll**: Payroll → Generate Payroll Button
2. **Process Payroll**: Click Process for draft records
3. **Mark as Paid**: Click Mark as Paid for processed records
4. **Download Reports**: Export → Download CSV/PDF

#### **Attendance Tracking**
1. **View Attendance**: Attendance → Select Date Range
2. **Manual Entry**: Add Attendance → Fill Details
3. **Generate Reports**: Reports → Attendance Report

### **Staff Functions**

#### **Personal Dashboard**
1. **Clock In/Out**: Dashboard → Clock In/Out Button
2. **View Attendance**: My Attendance → Calendar View
3. **Request Leave**: Leave → New Request
4. **Update Profile**: Profile → Edit Information

### **API Usage**

StaffSync provides REST API endpoints:

```bash
# Get all employees
GET /api/employees

# Get specific employee
GET /api/employee/{id}

# Add new employee
POST /api/employees/add

# Update employee
PUT /api/employee/{id}

# Delete employee
DELETE /api/employee/{id}

# Attendance endpoints
GET /api/attendance
POST /api/attendance/add

# Payroll endpoints
GET /api/payroll
POST /api/payroll/generate
```

---

## 🏗️ Project Structure

```
staffsync/
├── 📁 src/                          # Source code directory
│   ├── 📄 app.py                    # Main Flask application
│   ├── 📄 staffsync.db              # SQLite database
│   ├── 📁 config/                   # Configuration files
│   │   └── 📄 config.py             # App configuration
│   ├── 📁 static/                   # Static assets
│   │   ├── 📁 css/                  # Stylesheets
│   │   │   └── 📄 style.css         # Main stylesheet
│   │   └── 📁 js/                   # JavaScript files
│   │       └── 📄 script.js         # Main JavaScript
│   └── 📁 templates/                # Jinja2 templates
│       ├── 📄 base.html             # Base template
│       ├── 📄 login.html            # Login page
│       ├── 📄 register.html         # Registration page
│       ├── 📁 admin/                # Admin templates
│       │   ├── 📄 dashboard.html    # Admin dashboard
│       │   ├── 📄 employees.html    # Employee management
│       │   ├── 📄 payroll.html      # Payroll management
│       │   ├── 📄 attendance.html   # Attendance tracking
│       │   ├── 📄 departments.html  # Department management
│       │   └── 📄 settings.html     # System settings
│       └── 📁 staff/                # Staff templates
│           ├── 📄 dashboard.html    # Staff dashboard
│           ├── 📄 profile.html      # Profile management
│           ├── 📄 attendance.html   # Personal attendance
│           └── 📄 leave.html        # Leave management
├── 📄 run.py                        # Application runner
├── 📄 requirements.txt              # Python dependencies
├── 📄 setup.sh                      # Linux/macOS setup script
├── 📄 setup.bat                     # Windows setup script
├── 📄 README.md                     # This file
└── 📄 .gitignore                    # Git ignore rules
```

### **Key Files Explained**

- **`src/app.py`**: Main Flask application with all routes and business logic
- **`src/config/config.py`**: Configuration management for different environments
- **`run.py`**: Application entry point with environment setup
- **`src/static/css/style.css`**: Comprehensive CSS with modern design system
- **`src/static/js/script.js`**: Interactive JavaScript functionality
- **`requirements.txt`**: All Python package dependencies

---

## 🎨 Screenshots

### **Admin Dashboard**
*Modern analytics dashboard with real-time data visualization*

### **Employee Management**
*Comprehensive employee management with search and filtering*

### **Payroll System**
*Advanced payroll processing with automated calculations*

### **Mobile Interface**
*Fully responsive design works perfectly on all devices*

---

## 📖 API Documentation

### **Authentication Endpoints**

#### **Login**
```http
POST /login
Content-Type: application/json

{
    "username": "admin",
    "password": "admin123"
}
```

#### **Logout**
```http
GET /logout
```

### **Employee Endpoints**

#### **Get All Employees**
```http
GET /api/employees
Authorization: Session-based
```

#### **Get Employee by ID**
```http
GET /api/employee/{id}
Authorization: Session-based
```

#### **Add Employee**
```http
POST /api/employees/add
Content-Type: application/json

{
    "employee_id": "EMP001",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@company.com",
    "phone": "+1234567890",
    "position": "Developer",
    "department_id": 1,
    "salary": 50000
}
```

#### **Update Employee**
```http
PUT /api/employee/{id}
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Smith",
    "salary": 55000
}
```

#### **Delete Employee**
```http
DELETE /api/employee/{id}
Authorization: Admin only
```

### **Attendance Endpoints**

#### **Clock In/Out**
```http
POST /api/attendance/clock
Content-Type: application/json

{
    "employee_id": 1,
    "action": "clock_in"  // or "clock_out"
}
```

#### **Get Attendance Records**
```http
GET /api/attendance?employee_id=1&date=2025-10-31
Authorization: Session-based
```

### **Payroll Endpoints**

#### **Generate Payroll**
```http
POST /api/payroll/generate
Content-Type: application/json

{
    "pay_period_start": "2025-10-01",
    "pay_period_end": "2025-10-31",
    "employee_selection": "all"
}
```

#### **Get Payroll Records**
```http
GET /api/payroll
Authorization: Admin or Employee (own records)
```

### **Response Format**

All API endpoints return JSON responses in this format:

```json
{
    "success": true,
    "data": {
        // Response data
    },
    "message": "Operation completed successfully",
    "timestamp": "2025-10-31T12:00:00Z"
}
```

### **Error Responses**

```json
{
    "success": false,
    "error": "Error description",
    "code": "ERROR_CODE",
    "timestamp": "2025-10-31T12:00:00Z"
}
```

---

## 🧪 Testing

### **Running Tests**

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_employees.py

# Run with verbose output
pytest -v
```

### **Manual Testing Checklist**

#### **Authentication Testing**
- [ ] Admin login with correct credentials
- [ ] Staff login with correct credentials  
- [ ] Login failure with incorrect credentials
- [ ] Session management and logout
- [ ] Role-based access control

#### **Employee Management Testing**
- [ ] Add new employee
- [ ] Edit existing employee
- [ ] Delete employee (with confirmation)
- [ ] Search and filter employees
- [ ] View employee details

#### **Payroll Testing**
- [ ] Generate payroll for period
- [ ] Process payroll records
- [ ] Mark payroll as paid
- [ ] Download payslip
- [ ] Export payroll reports

#### **Attendance Testing**
- [ ] Clock in/out functionality
- [ ] Manual attendance entry
- [ ] View attendance calendar
- [ ] Generate attendance reports

### **Browser Testing**

Test on multiple browsers and devices:
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers (iOS/Android)

---

## 🚢 Deployment

### **Production Deployment**

#### **Option 1: Traditional Server (Ubuntu/CentOS)**

```bash
# 1. Install Python and dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv nginx

# 2. Clone and setup application
git clone https://github.com/Sumitdev09/staffsync.git
cd staffsync
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Install production server
pip install gunicorn

# 4. Create systemd service
sudo nano /etc/systemd/system/staffsync.service
```

**systemd service file:**
```ini
[Unit]
Description=StaffSync Flask Application
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/staffsync
Environment="PATH=/path/to/staffsync/venv/bin"
Environment="FLASK_ENV=production"
ExecStart=/path/to/staffsync/venv/bin/gunicorn --bind 127.0.0.1:5000 -w 4 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# 5. Start and enable service
sudo systemctl daemon-reload
sudo systemctl start staffsync
sudo systemctl enable staffsync

# 6. Configure Nginx
sudo nano /etc/nginx/sites-available/staffsync
```

**Nginx configuration:**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/staffsync/src/static;
        expires 30d;
    }
}
```

```bash
# 7. Enable site and restart nginx
sudo ln -s /etc/nginx/sites-available/staffsync /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### **Option 2: Docker Deployment**

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
```

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  staffsync:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-production-secret-key
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

Deploy with Docker:
```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

#### **Option 3: Cloud Deployment (Heroku)**

```bash
# 1. Install Heroku CLI
# 2. Login to Heroku
heroku login

# 3. Create Heroku app
heroku create your-staffsync-app

# 4. Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key

# 5. Create Procfile
echo "web: gunicorn run:app" > Procfile

# 6. Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# 7. Open application
heroku open
```

### **Environment-Specific Settings**

#### **Production Checklist**
- [ ] Change default passwords
- [ ] Set secure SECRET_KEY
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Set up database backups
- [ ] Configure logging
- [ ] Enable error monitoring
- [ ] Set up health checks

#### **Security Hardening**
```python
# Additional security headers
from flask_talisman import Talisman

# Enable security headers
Talisman(app)

# Rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **Getting Started**

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/staffsync.git
   ```
3. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make your changes**
5. **Test your changes**
   ```bash
   pytest
   ```
6. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
7. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Create a Pull Request**

### **Contribution Guidelines**

#### **Code Style**
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused

#### **Commit Messages**
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Add detailed description if needed

#### **Pull Request Process**
1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update README if necessary
5. Request review from maintainers

### **Types of Contributions**

- 🐛 **Bug Reports**: Report issues and bugs
- ✨ **Feature Requests**: Suggest new features
- 📖 **Documentation**: Improve docs and guides
- 🎨 **UI/UX**: Enhance user interface
- 🧪 **Testing**: Add or improve tests
- 🚀 **Performance**: Optimize code performance

### **Development Setup**

```bash
# Clone repository
git clone https://github.com/Sumitdev09/staffsync.git
cd staffsync

# Setup development environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Dev dependencies

# Run in development mode
python run.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### **MIT License**
```
MIT License

Copyright (c) 2025 StaffSync Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🆘 Support

### **Getting Help**

- 📖 **Documentation**: Check this README and inline code comments
- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Issues**: Report bugs via GitHub Issues
- 📧 **Email**: Contact maintainers directly

### **FAQ**

#### **Q: How do I change the default port?**
A: Set the `FLASK_PORT` environment variable or modify `src/config/config.py`

#### **Q: Can I use a different database?**
A: Yes, you can modify the database configuration in `src/config/config.py`

#### **Q: How do I add new features?**
A: Fork the repository, create a feature branch, implement your changes, and submit a pull request

#### **Q: Is this suitable for production?**
A: Yes, with proper configuration and security measures. See the deployment section.

#### **Q: How do I backup the database?**
A: Copy the `staffsync.db` file to a secure location regularly

#### **Q: Can I customize the UI?**
A: Yes, modify the CSS in `src/static/css/style.css` and templates in `src/templates/`

### **Troubleshooting**

#### **Common Issues**

**Database locked error:**
```bash
# Solution: Check if another instance is running
ps aux | grep python
kill -9 [process_id]
```

**Port already in use:**
```bash
# Solution: Find and kill the process
lsof -ti:5000 | xargs kill -9
```

**Permission denied errors:**
```bash
# Solution: Check file permissions
chmod +x setup.sh
```

**Module not found errors:**
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

---

<div align="center">

### **🚀 Ready to get started?**

[⬇️ Clone Repository](https://github.com/Sumitdev09/staffsync.git) • [📖 Read Docs](#-table-of-contents) • [🤝 Contribute](#-contributing) • [💬 Get Support](#-support)

**Made with ❤️ by the StaffSync Team**

⭐ **Star us on GitHub** if you find StaffSync useful!

</div> - Employee Management System

A comprehensive employee management system built with Python Flask, HTML, CSS, and MySQL. StaffSync provides a complete solution for managing employees, attendance, payroll, and administrative tasks with an attractive modern UI.

## 🌟 Features

### Admin Panel
- **Dashboard**: Overview of key metrics and statistics
- **Employee Management**: Add, edit, view, and manage employee records
- **Attendance Tracking**: Monitor daily attendance with check-in/check-out times
- **Payroll Management**: Generate payroll, process salaries, and manage payments
- **Department Management**: Organize employees by departments
- **Reports & Analytics**: Generate various reports and visualizations
- **User Management**: Manage admin and staff user accounts

### Staff Panel
- **Personal Dashboard**: View personal information and statistics
- **Attendance Marking**: Easy check-in/check-out system
- **Attendance History**: View personal attendance records
- **Leave Requests**: Submit and track leave applications
- **Payroll Information**: View salary slips and payment history
- **Profile Management**: Update personal information

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design
- **Charts**: Chart.js for data visualization
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/staffsync.git
cd staffsync
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Create MySQL Database
```sql
CREATE DATABASE staffsync;
```

#### Import Database Schema
```bash
mysql -u root -p staffsync < database/staffsync.sql
```

#### Configure Database Connection
Edit the database configuration in `app/app.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',
    'database': 'staffsync',
    'autocommit': True
}
```

### 5. Run the Application
```bash
cd app
python app.py
```

The application will be available at `http://localhost:5000`

## 🔐 Default Login Credentials

**Administrator Account:**
- Username: `admin`
- Password: `admin123`

⚠️ **Important**: Change these default credentials after first login for security.

## 📁 Project Structure

```
staffsync/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css          # Modern CSS styling
│   │   └── js/
│   │       └── script.js          # JavaScript functionality
│   ├── templates/
│   │   ├── admin/
│   │   │   ├── dashboard.html     # Admin dashboard
│   │   │   ├── employees.html     # Employee management
│   │   │   ├── attendance.html    # Attendance management
│   │   │   └── payroll.html       # Payroll management
│   │   ├── staff/
│   │   │   └── dashboard.html     # Staff dashboard
│   │   ├── base.html              # Base template
│   │   └── login.html             # Login page
│   └── app.py                     # Main Flask application
├── database/
│   └── staffsync.sql              # Database schema
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🎨 UI Features

- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Smooth animations and hover effects
- **Data Visualization**: Charts and graphs for analytics
- **Real-time Updates**: Live clock and status updates
- **Notification System**: Toast notifications for user feedback

## 🔧 Key Functionalities

### Employee Management
- Add new employees with complete information
- Edit existing employee records
- View employee profiles and history
- Manage department assignments
- Track employee status (active/inactive)

### Attendance System
- Real-time attendance marking
- Check-in/check-out time tracking
- Attendance history and reports
- Late arrival detection
- Absence management

### Payroll Processing
- Automated salary calculations
- Overtime pay computation
- Tax deduction handling
- Allowances and deductions
- Payslip generation
- Payment status tracking

### Security Features
- User authentication and authorization
- Role-based access control (Admin/Staff)
- Session management
- Password hashing
- Activity logging

## 📊 Database Schema

The system uses a relational database with the following main tables:

- **users**: Authentication and user roles
- **employees**: Employee personal and professional information
- **departments**: Department organization
- **attendance**: Daily attendance records
- **payroll**: Salary and payment information
- **leave_requests**: Leave applications and approvals
- **activity_logs**: System activity tracking
- **settings**: Application configuration

## 🔒 Security Considerations

- All passwords are hashed using bcrypt
- SQL injection protection through parameterized queries
- Session-based authentication
- Role-based access control
- Input validation and sanitization
- CSRF protection (implement as needed)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or need help setting up the system:

1. Check the troubleshooting section below
2. Review the database configuration
3. Ensure all dependencies are installed
4. Verify MySQL server is running

## 🔧 Troubleshooting

### Common Issues

**Database Connection Error:**
- Verify MySQL server is running
- Check database credentials in `app.py`
- Ensure database `staffsync` exists

**Module Not Found Error:**
- Activate virtual environment
- Install requirements: `pip install -r requirements.txt`

**Permission Denied:**
- Check file permissions
- Ensure proper database user privileges

**CSS/JS Not Loading:**
- Check static file paths
- Clear browser cache
- Verify Flask static folder configuration

## 🚀 Future Enhancements

- Email notifications for important events
- Advanced reporting and analytics
- Mobile app integration
- Biometric attendance system
- Performance appraisal module
- Training and development tracking
- Document management system
- Multi-language support

## 👥 Authors

- **Your Name** - Initial work - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Font Awesome for icons
- Chart.js for data visualization
- Google Fonts for typography
- Flask community for excellent documentation