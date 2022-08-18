import socket
from pathlib import Path
from utils import extract_route, read_file, load_data, build_response
from views import index

CUR_DIR = Path(__file__).parent
SERVER_HOST = 'localhost'
SERVER_PORT = 8080

getit, note = open('index.html', 'r', encoding="utf-8"), open('note.html', 'r', encoding="utf-8")
getit_content, note_content = getit.read(), note.read()
getit.close()
note.close()
RESPONSE_TEMPLATE = 'HTTP/1.1 200 OK' + '\n' + 'Content-Type: text/html' + '\n' + '\n' + getit_content

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    else:
        response = build_response()
    client_connection.sendall(response)
    client_connection.close()