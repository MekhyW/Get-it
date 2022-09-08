import sqlite3
import flask
from flask_cors import CORS, cross_origin
app = flask.Flask('getit_backend')
cors = CORS(app)

def run_query(connection, query):
    cursor = connection.execute(query)
    connection.commit()
    return cursor

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

conn = sqlite3.connect('db.sqlite', check_same_thread=False)
run_query(conn, "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
original_index = open('index_empty.html', 'r', encoding="utf8").read()

def get_all():
    cursor = run_query(conn, "SELECT * FROM note")
    notes = []
    for id, title, content in cursor:
        notes.append(Note(id, title, content))
    return notes

def constructIndex():
    notes = get_all()
    html_notes = ''
    note_example = open('note_example.html', 'r', encoding="utf8").read()
    for note in notes:
        html_notes += note_example.replace('titulo', note.title).replace('detalhes', note.content).replace('ID', str(note.id))
        html_notes += '\n'
    index = original_index.replace('<!-- card-container -->', html_notes)
    open('index.html', 'w', encoding="utf8").write(index)

def add(note):
    run_query(conn, "INSERT INTO note (title, content) VALUES ('{}', '{}')".format(note.title, note.content))

def update(entry):
    run_query(conn, "UPDATE note SET title = '{}', content = '{}' WHERE id = {}".format(entry.title, entry.content, entry.id))

def delete(note_id):
    run_query(conn, "DELETE FROM note WHERE id = {}".format(note_id))


@app.route('/create', methods=['POST'])
@cross_origin()
def create():
    add(Note(title=flask.request.json['title'], content=flask.request.json['content']))
    constructIndex()
    return 'ok'

@app.route('/edit', methods=['POST'])
def edit():
    update(Note(id=flask.request.json['id'], title=flask.request.json['title'], content=flask.request.json['content']))
    constructIndex()
    return 'ok'

@app.route('/trash', methods=['POST'])
def trash():
    delete(flask.request.json['id'])
    constructIndex()
    return 'ok'

if __name__ == '__main__':
    constructIndex()
    app.run(host='0.0.0.0', port=80)