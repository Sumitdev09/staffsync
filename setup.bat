@echo off
REM StaffSync Environment Setup Script for Windows
REM This script sets up the development environment for StaffSync

echo 🚀 Setting up StaffSync development environment...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📥 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Environment setup complete!
echo.
echo 🎯 Next steps:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Run the application: python run.py
echo 3. Open your browser and go to: http://localhost:5000
echo.
echo 🔐 Default login credentials:
echo    Admin: admin / admin123
echo    Staff: john.doe / pass123

pause