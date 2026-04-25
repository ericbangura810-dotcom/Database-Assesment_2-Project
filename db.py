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

    cur.execute('''
Create TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL,
role TEXT NOT NULL,
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS warehouses (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
address_encrypted TEXT NOT NULL,
phone TEXT NOT NULL,
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS warehouse_inventory (
id INTEGER PRIMARY KEY,
warehouse_id INTEGER NOT NULL,
item_id INTEGER NOT NULL,
quantity INTEGER NOT NULL DEFAULT 0,
FOREIGN KEY (warehouse_id) REFERENCES warehouses (id)
FOREIGN KEY (item_id) REFERENCES items (id)
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS items (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
description TEXT NOT NULL,
reorder_level INTEGER DEFAULT 0,
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS vehicles (
id INTEGER PRIMARY KEY,
registration TEXT NOT NULL,
capacity INTEGER NOT NULL,
maintenance_date TEXT NOT NULL,
status TEXT NOT NULL,'
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS drivers (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
license_number TEXT NOT NULL,
phone_encrypted TEXT NOT NULL,
address_encrypted TEXT NOT NULL,
active INTEGER NOT NULL,
)
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS driver_assignments (
id INTEGER PRIMARY KEY,
driver_id INTEGER NOT NULL,
vehicle_id INTEGER NOT NULL,
shift_start TEXT NOT NULL,
shift_end TEXT NOT NULL,
route_description TEXT NOT NULL,
FOREIGN KEY (driver_id) REFERENCES drivers (id)
FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)
)
''')

    cur.execute('''''')