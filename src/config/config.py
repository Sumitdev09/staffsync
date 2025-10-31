# StaffSync Configuration
import os
from datetime import timedelta

class Config:
    """Base configuration class."""
    
    # Application settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'
    
    # Database settings
    DATABASE_PATH = 'staffsync.db'
    
    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # Debug mode (set to False in production)
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # Host and port settings
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))
    
    # Application information
    APP_NAME = "StaffSync"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "Modern Employee Management System"

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-change-this-in-production'

class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    DATABASE_PATH = 'test_staffsync.db'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}