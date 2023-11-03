import sqlite3
from encryption import *

conn = sqlite3.connect("db/users.db")
c = conn.cursor()


def userInfo(username):
    try:
        c.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {username} (
                site TEXT,
                password TEXT
        )"""
        )

        c.execute(
            f"""
            SELECT * FROM {username}
        """
        )

        conn.commit()
        info = c.fetchall()
        return info

    except:
        return "Failed to fetch user data."


def addSite(username, site, password):
    try:
        c.execute(
            f"""
        INSERT INTO {username} (site, password)
        VALUES (?, ?);
        """,
            (encrypt(site), encrypt(password)),
        )
        conn.commit()
        return "Success!"

    except:
        return "Error"


def removeSite(username, site, password):
    try:
        c.execute(
            "DELETE FROM {} WHERE site = ? AND password = ?".format(username),
            (encrypt(site), encrypt(password)),
        )
        conn.commit()
        if c.rowcount == 1:
            return "Success!"
        else:
            return "No matching record found."
    except sqlite3.Error as e:
        return "Error: " + str(e)
