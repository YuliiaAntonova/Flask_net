import sqlite3
import os

ROOT = os.path.dirname(os.path.realpath(__file__))


def create_post(name, content):
    conn = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('insert into posts (name,content) values(?,?)', (name, content))
    conn.commit()
    conn.close()


def get_posts():
    conn = sqlite3.connect(os.path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts

