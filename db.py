import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), 'northshore_locations.db')

print("Using DB at:", DB_NAME)

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()


