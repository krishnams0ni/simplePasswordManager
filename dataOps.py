import sqlite3

conn = sqlite3.connect('db/users.db')
c = conn.cursor()


def userInfo(username):
    try:
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {username} (
                site TEXT,
                password TEXT
        )""")

        c.execute(f"""
            SELECT * FROM {username}
        """)

        conn.commit()
        info = c.fetchall()
        return info

    except:
        return "Failed to fetch user data."


def addSite(username, site, password):
    try:
        c.execute(f"""
        INSERT INTO {username} (site, password)
        VALUES (?, ?);
        """, (site, password))
        conn.commit()
        return "Success!"

    except:
        return "Error"


def removeSite(username, site, password):
    try:
        c.execute(f"""
            DELETE FROM {username} WHERE site = ? AND password = ?;
        """, (site, password))
        conn.commit()
        return "Success!"

    except:
        return "Error"
