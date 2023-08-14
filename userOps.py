import sqlite3

import dataOps

conn = sqlite3.connect('db/users.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        username TEXT PRIMARY KEY,
        name TEXT,
        password TEXT,
        email TEXT
);""")
conn.commit()


def addUser(name, username, password, confirmPassword, email):
    if password != confirmPassword:
        return "The passwords don't match."

    try:
        c.execute("""
            SELECT username FROM Users WHERE username = ?;
        """, (username,))
        user = c.fetchone()

        if user:
            return "Username already taken."

        c.execute("""
            INSERT INTO Users (name, username, password, email)
            VALUES (?, ?, ?, ?);
        """, (name, username, password, email))
        conn.commit()
        return "Welcome " + name + "!"

    except:
        return "Error adding user: " + name


def removeUser(username, password, confirmPassword):
    if password != confirmPassword:
        return "The passwords don't match."

    try:
        c.execute("""
            SELECT username, password FROM Users WHERE username = ? AND password = ?
        """, (username, password))
        user = c.fetchone()

        if not user:
            return "User not found."

        c.execute("""
            SELECT name FROM Users WHERE username = ?
        """, (username,))
        user = c.fetchone()[0]
        c.execute("""
            DELETE FROM Users WHERE username = ?
        """, (username,))
        conn.commit()

        return "Sorry to see you go " + user + "!"

    except:
        return "Error removing user: " + username


def loginPortal(username, password):
    c.execute("""
        SELECT username, password FROM Users WHERE username = ? AND password = ?
        """, (username, password))
    user = c.fetchone()

    if not user:
        return "Invalid credentials."
    elif username == "Users":
        return "Choose a different username"
    return dataOps.userInfo(username)

# result = addUser("Alice", "alice", "password123", "password123", "alice")
# result = removeUser("alice", "password123", "password123")
# result = loginPortal("alice", "password123")
# dataOps.addSite("alice", "google", "passkey")
# dataOps.addSite("alice", "facebook", "facekey")
# dataOps.removeSite("alice", "google", "passkey")
# result = dataOps.userInfo("alice")
# print(result)
