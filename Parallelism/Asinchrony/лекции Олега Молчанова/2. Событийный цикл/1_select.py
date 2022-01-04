import socket
from select import select

"""
На этом уроке мы сделаем так, чтобы функции для клиентсого и серверного 
сокетов не зависели друг от друга.

select - это системная функция, которая нужна для мониторинга 
изменений состояний файловых объектов (сокетов), которые мы в нее передадим
на вход функция select получает 3 списка. Эти списки - это те объекты, за изменением 
состояний которых нужно следить:
1) те объекты, за которыми нужно следить, когда они станут доступными для чтения.
Вот сюда мы и передадим список с сокетами, а конкретно [server_socket]
Что значит чтение? Пользователь если что-то напишет, то мы это и будем читать.
2) те объекты, за которыми нужно следить, когда они станут доступными для записи.
3) объекты, у которых мы ожидаем какие-то ошибки
В данном уроке пункты 2 и 3 нас не интересуют.

Эта функция возвращает те же самые объекты, но после того как они станут доступны.
"""

# переменная для мониторинга, в которую будет передан срверный сокет
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))  # в этот момент создается файл сокета
server_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', client_socket, addr)

    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    """Здесь происходит управление accept_connection и send_message."""
    while True:
        # распаковываем то, что нам вернет select
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors
        for sock in ready_to_read:
            # если у нас оказался серверный сокет, то устанавливаем соединение
            if sock is server_socket:
                accept_connection(sock)
            # если нам попадется клиентский сокет, то отправляем сообщение
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()

# теперь наше приложение работает асинхронно в одном потоке
