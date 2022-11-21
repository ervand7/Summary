import socket
from select import select

tasks = []

dict_to_read = {}  # сокеты и генераторы для чтения
dict_to_write = {}  # сокеты и генераторы для записи


def server():
    """Создание серверного сокета."""
    # 4 строки из первого урока
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:
        # в yield вместе с server_socket возвращаем текстовую метку 'read'
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept()  # read
        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    # клиентский сокет может быть в 2 состояниях: когда он читает и пишет
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096)  # read
        if not request:
            print('not request')
            break
        else:
            response = 'Hello world\n'.encode()
            yield ('write', client_socket)
            client_socket.send(response)
    client_socket.close()


def event_loop():
    while any([tasks, dict_to_read, dict_to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(dict_to_read, dict_to_write, [])
            for sock in ready_to_read:
                tasks.append(dict_to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(dict_to_write.pop(sock))

        try:
            # получаем первое задание
            task = tasks.pop(0)
            reason, sock = next(task)  # ('write', client_socket)
            if reason == 'read':
                dict_to_read[sock] = task
            if reason == 'write':
                dict_to_write[sock] = task
        except StopIteration:
            print('Done!')


tasks.append(server())
event_loop()
