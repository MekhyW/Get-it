from cProfile import run
import sqlite3

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

def run_query(connection, query):
    cursor = connection.execute(query)
    connection.commit()
    return cursor

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite')
        run_query(self.conn, "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
    def add(self, note):
        run_query(self.conn, "INSERT INTO note (title, content) VALUES ('{}', '{}')".format(note.title, note.content))
    def get_all(self):
        cursor = run_query(self.conn, "SELECT * FROM note")
        notes = []
        for id, title, content in cursor:
            notes.append(Note(id, title, content))
        return notes
    def update(self, entry):
        run_query(self.conn, "UPDATE note SET title = '{}', content = '{}' WHERE id = {}".format(entry.title, entry.content, entry.id))
    def delete(self, note_id):
        run_query(self.conn, "DELETE FROM note WHERE id = {}".format(note_id))