import os
import json

import sqlite3
from sqlite3 import Error

CONFIG = json.load(open("config.json"))
DB_PATH = CONFIG.get("database_path")


def setup_bd ():
    if not os.path.exists(DB_PATH):
        os.mkdir(DB_PATH)
        
    tables = CONFIG.get("tables")
    for table in tables:
        create_table(table, tables.get("table"))


def create_connection (file="data.db"):
    path = DB_PATH + file
    connection = None

    try:
        connection = sqlite3.connect(path)
    except Error as e:
        # TODO: replace prints with logs
        print(f"The error '{e}' occurred.")
    
    return connection


def create_table (name, columns):
    conn = create_connection()
    assert conn is not None, "cannot create connection with SQLite DB"

    columns = str(columns).strip("[]")

    c = conn.cursor()
    c.execute(f"CREATE TABLE IF NOT EXISTS {name} ({columns})")
    conn.commit()
    conn.close()
