import socket
from select import select
"""
Перед нами возникает 2 задачи:
1) нам нужно определить, какие сокеты уже готовы для чтения и записи и 
вызвать соответствующие методы (accept, recv, send)
Эту проблему мы будем решать с помощью функции select()
2) нам нужен механизм, который мог бы переключать управление между функциями
(server() и client())
Эту проблему мы будем решать с помощью генератора и событийного цикла.

Сокеты мы будет передавать в функцию select. select будет нам возвращать те из
них, которые готовы.
"""
"""
Чего мы добились с помощью инструкций yield.
Когда выполнение функции доходит до блокирующей операции (accept, recv, send)
и мы ждем соединения, то перед тем как вызывается блокирующий метод, генератор
отдает нам кортеж с сокетом. То есть, вместо того, чтобы зависнуть в ожидании,
генератор отфутболивает контроль управления (вместе с сокетом) обратно туда,
откуда мы вызываем функцию next. И в этот момент функция ставится на паузу.
И ее выполнение в следующий раз продолжится только тогда, когда сокет будет
готов выполнить этот метод без задержек. И наша задача сводится к тому,
чтобы поймать этот сокет и передать его в функцию select. select нам сделает 
выборку тех сокетов, которые уже готовы, и мы просто вызываем функцию next
у соответствующего генератора.
"""

# обычно для такого дела используют очереди (from collections import deque)
# этот список будет наполняться генераторами. Из этого списка мы будем брать
# первый элемент и передавать его в next
tasks = []

"""
У нас возникает пара сущностей, связанных между собой:
сокет и функция, которая обслуживает этот 
сокет(server_socket-server(), client_socket-client()). Поэтому будем их хранить в словарях
словариdict_to_read и dict_to_write будут неким сырьем для tasks. Из этих словарей
мы будем извлекать генераторы и добавлять в список tasks
"""
dict_to_read = {}  # сокеты и генераторы для чтения
dict_to_write = {}  # сокеты и генераторы для записи


def server():
    """Создание серверного сокета."""
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
    # клиентский сокет может быть в 2 состояниях: когда он читает и пришет
    while True:
        # в yield вместе с client_socket возвращаем текстовую метку 'read'
        yield ('read', client_socket)
        request = client_socket.recv(4096)  # read
        if not request:
            print('not request')
            break
        else:
            response = 'Hello world\n'.encode()
            # в yield вместе с client_socket возвращаем текстовую метку 'read'
            yield ('write', client_socket)
            client_socket.send(response)  # write  # send - это тоже блокирующая операция
    client_socket.close()


def event_loop():
    # сюда передаем глобальные переменные
    while any([tasks, dict_to_read, dict_to_write]):
        print(f'tasks {tasks}\n')
        print(f'dict_to_read {dict_to_read}\n')
        print(f'dict_to_write {dict_to_write}\n')
        # мы должны обеспечить работой наш событийный цикл
        # поэтому давайте наполним список tasks генераторами
        while not tasks:
            # передаем в select первыми двумя аргументами словари, так как далее в цикле
            # мы получим их ключи, а нам как раз только ключи и нужны
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

"""
Расписываю по шагам, что происходит в этом скрипте:
1. Запускаем окно с основным сервером командой <python3 4_async_gens.py>
1.1 После инициализации переменныхdict_to_read=to_write={} первым делом в программе 
запускается строка <tasks.append(server())> (см. предпоследнюю строку) и наш tasks выглядит так: 
tasks [<generator object server at 0x7f8582c92eb0>]
В это время словари dict_to_read и dict_to_write еще равны {}
1.2 Запускается функция event_loop() и в ней первым делом срабатывает конструкция try-except, 
и наш список tasks становится пустым, так как мы там делаем <task = tasks.pop(0)>.
1.3 Словарьdict_to_read становится таким:
key:
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001)>
value:
<generator object server at 0x7f8582c92eb0>}
И все это из-за того что:
а) у нас в пункте 1.1 при добавлении в список tasks инициализировалась
функция server() и yield вернул кортеж ('read', server_socket)
б) в конструкции try-except из event_loop() мы вывили, что <reason == 'read'>

2 Запускаем первого клиента через второе окно терминала командой <nc localhost 5001>
2.1 В первом окне терминала получаем сообщение
Connection from ('127.0.0.1', 57249)
Мы получили это сообщение из-за того, что в функции server в бесконечном цикле у нас 
accept() работает на 'read'. То есть он работает на чтение. Вот он и прочел что должен был 
прочесть, и следующей строкой выдал то, что мы запрограммировали: 
<print('Connection from', addr)>
2.2 Список tasks у нас стал таким:
tasks [<generator object client at 0x7faf5c48add0>]
То есть, в него уже в отличие от пункта "1" попал не серверный, а клиентский сокет.
Это произошло из-за того что мы до сих пор (и до тех пор пока мы не остановим всю программу)
находимся во внешнем бесконечном цикле функции event_loop(). И тут мы видим, что:
а) в конструкции try-except из мы сделали все, что должны были сделать, 
и наш список tasks стал пустым
б) нас соответственно перекинуло во внешний бесконечный цикл
в) тут мы видим условие:
<ready_to_read, ready_to_write, _ = select(dict_to_read, dict_to_write, [])>
при котором вункция select нам возвращает сокеты, готовые к употреблению.
И тут уже на плечи библиотеки select ложится ответственность, какой "готовый к употреблению"
сокет мы получим. И берем самый последний. И в нашем текущем случае самым последним 
оказывается клиентский, что нам и нужно.
Важно понимать, что принцип Round Robin у нас реализуется именно вdict_to_read. 
Сейчас вdict_to_read будут меняться местами серверный и клиентский сокеты.

3 Пишем во втором окне терминала сообщение и нажимаем Enter
3.1 Словарь dict_to_write принимает
key:
<socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001), raddr=('127.0.0.1', 57648)>
value:
<generator object client at 0x7f998bc91dd0>
и клиенту отправляется сообщение "Hello world", так как мы это прописали в условии
else:
    response = 'Hello world\n'.encode()
    yield ('write', client_socket)
    client_socket.send(response) <-----
    
4. Открываем третье окно термнала и запускаем командой <nc localhost 5001>
4.1 Теперь по принципу Round Robin, который у нас реализуется вdict_to_read,
вdict_to_read будут меняться местами 3 сокета: серверный, первого клиента и второго клиента
иdict_to_read будет выглядеть так:
{
 <socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001), raddr=('127.0.0.1', 57648)>: <generator object client at 0x7f998bc91dd0>, 
 <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001)>: <generator object server at 0x7f998bc91eb0>, 
 <socket.socket fd=8, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5001), raddr=('127.0.0.1', 57694)>: <generator object client at 0x7f998bc91d60>
}
 
"""

