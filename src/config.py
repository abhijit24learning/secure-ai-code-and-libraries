"""Configuration module - VULNERABLE VERSION"""
import pickle
import os

# ⚠️ B105: Hardcoded password
DB_PASSWORD = "prod_password_12345"
DB_HOST = "database.prod.aws.amazonaws.com"

# ⚠️ B106: Hardcoded password in function default
def connect_database(username, password="admin123"):
    """Connect to database with hardcoded default password"""
    import sqlite3
    return sqlite3.connect(":memory:")

# ⚠️ B105: Hardcoded AWS credentials
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# ⚠️ B105: Hardcoded API Token
API_TOKEN = "sk_live_4eC39HqLyjWDarhtT657jjke"
