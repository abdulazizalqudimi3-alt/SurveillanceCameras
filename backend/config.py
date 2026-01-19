import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key-change-me')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    PORT = int(os.environ.get('PORT', 5000))

    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'default-jwt-secret-key-change-me')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/enhanced_security_system.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload settings
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    MAX_FILE_SIZE = int(os.environ.get('MAX_FILE_SIZE', 32 * 1024 * 1024))
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

    # SMTP settings
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    FROM_EMAIL = os.environ.get('FROM_EMAIL')
    FROM_NAME = os.environ.get('FROM_NAME', 'نظام الإنذار والأمان الذكي')

    # Model settings
    MODELS_DIR = os.environ.get('MODELS_DIR', 'models')
