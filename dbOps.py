import sqlite3

conn = sqlite3.connect('db/users.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        name TEXT,
        password TEXT
);""")
conn.commit()


def addUser(name, password, confirmPassword):
    if password != confirmPassword:
        return "The passwords don't match."

    try:
        c.execute("""
            SELECT name FROM Users WHERE name = ?;
        """, (name,))
        user = c.fetchone()

        if user:
            return "User already exists."

        c.execute("""
            INSERT INTO Users (name, password)
            VALUES (?, ?);
        """, (name, password))
        conn.commit()
        return "Welcome " + name + "!"

    except:
        return "Error adding user: " + name


def removeUser(name, password, confirmPassword):
    if password != confirmPassword:
        return "The passwords don't match."

    try:
        c.execute("""
            SELECT * FROM Users WHERE name = ? AND password = ?
        """, (name, password))
        user = c.fetchone()

        if not user:
            return "User not found."

        c.execute("""
            DELETE FROM Users
            WHERE name = ? AND password = ?;
        """, (name, password))
        conn.commit()
        return "Sorry to see you go " + name + "!"

    except:
        return "Error removing user: " + name


# addUser("Alice", "password123", "password123")
# removeUser("Alce", "password123", "password123")
# result = removeUser("Alice", "password123", "password123")
# print(result)
