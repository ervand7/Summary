import selectors
import socket

"""
Особенность этого примера в том, что мы регистрируем сокеты с 
сопровождающими данными (в параметре data)
"""


selector = selectors.DefaultSelector()


def server():
    # 4 строки из первого урока
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    # регистрируем сокет сервера
    selector.register(
        fileobj=server_socket,
        events=selectors.EVENT_READ,  # нас интересует чтение
        data=accept_connection  # data - любые связанные с сокетом данные
        # в нашем случае это функция accept_connection без вызова
    )


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', client_socket, addr)

    # регистрируем сокет клиента
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        # прежде чем закрыть сокет, мы его снимаем с регистрации
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            # получаем обратно нашу функцию
            callback = key.data  # data - то же самое, что и data из selector.register
            # то есть callback = accept_connection или send_message но уже после обработки
            callback(key.fileobj)  # вызываем callback передавая в него сам сокет


if __name__ == '__main__':
    server()
    event_loop()

# теперь наше приложение работает асинхронно в одном потоке
