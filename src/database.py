"""Database operations - VULNERABLE VERSION"""
import sqlite3

class UserRepository:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')

    # ⚠️ B608: SQL Injection vulnerability
    def find_user_by_email(self, email):
        """Find user by email - VULNERABLE to SQL injection"""
        # Attacker: email = "' OR '1'='1' --"
        query = f"SELECT * FROM users WHERE email = '{email}'"
        cursor = self.conn.cursor()
        return cursor.execute(query).fetchone()

    # ⚠️ B608: SQL Injection vulnerability
    def find_user_by_id(self, user_id):
        """Find user by ID - VULNERABLE to SQL injection"""
        # Attacker: user_id = "1 OR 1=1"
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor = self.conn.cursor()
        return cursor.execute(query).fetchone()

    # ⚠️ B608: SQL Injection vulnerability
    def filter_users_by_status(self, status):
        """Filter users by status - VULNERABLE to SQL injection"""
        query = "SELECT * FROM users WHERE status = '" + status + "'"
        cursor = self.conn.cursor()
        return cursor.execute(query).fetchall()
