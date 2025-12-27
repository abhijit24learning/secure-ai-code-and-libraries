"""Utility functions - VULNERABLE VERSION"""
import hashlib
import os
import subprocess

# ⚠️ B303: Use of insecure MD5 hash
def hash_password_weak(password):
    """Hash password using weak MD5 - NOT secure for passwords"""
    return hashlib.md5(password.encode()).hexdigest()

# ⚠️ B602: Command injection vulnerability
def process_image(filename, user_input):
    """Process image with command injection risk"""
    # Attacker: user_input = "; rm -rf /"
    command = f"convert {filename} -filter {user_input} output.jpg"
    result = os.system(command)  # Shell interprets metacharacters
    return result

# ⚠️ B602: Unsafe subprocess with shell=True
def run_training_script(script_name):
    """Run training script - vulnerable to command injection"""
    cmd = f"python scripts/{script_name}"
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout

# ⚠️ CWE-20: Missing input validation
def create_user(username, email, role):
    """Create user without proper validation"""
    # No validation on role parameter
    query = f"INSERT INTO users VALUES ('{username}', '{email}', '{role}')"
    return query
