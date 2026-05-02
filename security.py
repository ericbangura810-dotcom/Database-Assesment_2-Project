import hashlib
from db import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password, stored_hash):
    return hash_password(password) == stored_hash

KEY = 5

def encrypt_text(text):
    if text is None:
        return None
    return "".join(chr(ord(c) ^ KEY) for c in text)

def decrypt_text(text):
    if text is None:
        return None
    return "".join(chr(ord(c) ^ KEY) for c in text)
