import socket


SERVER_HOST = '192.168.1.117'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)


while True:    
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    lines = request.split('\n')
    command = lines[0].split(' ')
    print(request)

    if command[1] == '/':
        fin = open('index.html','rb')
    else:
        fin = open(command[1][1:],'rb')

    fileSource = fin.read()
    fin.close()

    response = 'HTTP/1.0 200 OK\n\n'.encode() + fileSource
    client_connection.sendall(response)
    client_connection.close()

server_socket.close()