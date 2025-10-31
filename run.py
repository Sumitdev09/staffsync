#!/usr/bin/env python3
"""
StaffSync - Modern Employee Management System
Run script for the Flask application
"""

import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app import app
from config.config import config

def main():
    """Main function to run the Flask application."""
    
    # Get environment (default: development)
    env = os.environ.get('FLASK_ENV', 'development')
    
    # Load configuration
    app_config = config.get(env, config['default'])
    
    # Apply configuration
    app.config.from_object(app_config)
    
    print("🚀 Starting StaffSync Employee Management System...")
    print("=" * 60)
    print("📋 Login Credentials:")
    print("   👑 Admin - Username: admin, Password: admin123")
    print("   👤 Staff - Username: john.doe, Password: pass123")
    print("   👤 Staff - Username: jane.smith, Password: pass123")
    print("   👤 Staff - Username: mike.johnson, Password: pass123")
    print("   👤 Staff - Username: sarah.wilson, Password: pass123")
    print("   👤 Staff - Username: david.brown, Password: pass123")
    print(f"🌐 Access URL: http://localhost:{app_config.PORT}")
    print(f"📝 Registration: http://localhost:{app_config.PORT}/register")
    print("=" * 60)
    
    # Run the application
    app.run(
        host=app_config.HOST,
        port=app_config.PORT,
        debug=app_config.DEBUG
    )

if __name__ == '__main__':
    main()