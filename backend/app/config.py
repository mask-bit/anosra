import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///anosra.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = False  # Token nunca expira
    OPEN_FINANCE_API_URL = os.getenv('OPEN_FINANCE_API_URL')
    OPEN_FINANCE_CLIENT_ID = os.getenv('OPEN_FINANCE_CLIENT_ID')
    OPEN_FINANCE_CLIENT_SECRET = os.getenv('OPEN_FINANCE_CLIENT_SECRET')
