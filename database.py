# database.py

import sqlite3

def init_db():
    conn = sqlite3.connect("chat_history.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def save_chat(user_msg, bot_reply):

    conn = sqlite3.connect("chat_history.db")

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chats
    (user_message, bot_response)
    VALUES (?,?)
    """, (user_msg, bot_reply))

    conn.commit()
    conn.close()

def get_chat_history():

    conn = sqlite3.connect("chat_history.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_message, bot_response, timestamp
    FROM chats
    ORDER BY id DESC
    """)

    history = cursor.fetchall()

    conn.close()

    return history