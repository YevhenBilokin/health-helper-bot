import sqlite3
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.config import DB_PATH

#Create and check database if it exists 
def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,  
        gender TEXT,                  
        weight REAL                   
    )
    ''')

    conn.commit()
    conn.close()

def save_useer_data(user_id, gender, weight):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO users (user_id, gender, weight) 
    VALUES (?, ?, ?)
    ON CONFLICT(user_id) 
    DO UPDATE SET gender = ?, weight = ?
    ''', (user_id, gender, weight, gender, weight))
    
    conn.commit()
    conn.close()

def get_user_data(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    
    return user_data


if __name__ == "__main__":
    create_table()