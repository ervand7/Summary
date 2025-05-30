import socket

"""
В этом модуле мы опишем проблему, которая возникает если не использовать асинхронность.
"Кооперативная многозадачность в рамках одного процесса". Не путать, здесь не будет идти речь о
много поточности и многопроцессности.
"""
# сокет (гнездо) - это пара хост:порт
# Настраиваем server_socket: AF_INET - ip-протокол 4 версии, SOCK_STREAM говорит,
# что речь пойдет о поддержке  tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SO_REUSEADDR - переиспользование адреса. Чтобы если мы прервем работу скрипта,
# чтоб можно было сразу использовать порт
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# указываем, к какому домену и порту мы привяжем сокет
server_socket.bind(('localhost', 5001))
# указываем сокетному серверу чтобы он начал прослушивать входящий буфер на предмет входящих подключений
server_socket.listen()

# мы расписали серверный сокет
# теперь давайте распишем клиентский сокет
while True:
    print('Before calling .accept()')
    # accept блокирует выполнение нашей программы пока мы не получим ответ от клиента
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    while True:
        # сейчас, без использования асинхронности
        # мы будем заперты внутри этого цикла пока клиент не отключится. Только когда он отрубится,
        # мы сможем подняться на уровень внешнего цикла и обработать второго клиента
        print('Before calling .recv()')
        # настраиваем запрос пользователя. Клиентский сокет принимает сообщение размером в 4 килобайта
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    print('Outside inner while loop')
    # закрываем клиентский сокет, иначе сервер подумает, что мы просто медленно отвечаем
    client_socket.close()

# открываем 3 окна терминала: 1-для сервера, 2-для первого клиента, 3-для второго клиента
# в 1 окне вызываем: <python3 original.py>
# в 2 окне вызываем: <nc localhost 5001>, печатаем что-то, нажимаем Enter и видим, что сервер нам отвечает "Hello world"
# в 3 окне вызываем: <nc localhost 5001>, печатаем что-то, нажимаем Enter и видим, что сервер нам не отвечает
# и только после того как отрубится 1й клиент из второго окна, сервер
# сможет обрабатывать запросы 2го клиента из третьего окна. Вот и суть проблемы

# Получается, что нам нужен некий код-менеджер, который бы рулил контролем
# выполнения в период ожидания. И этот код принято называть <Event loop> или событийным циклом.

# Асинхронный код можно писать без использования сторонних библиотек 3 способами:
# 1) с помощью колбеков
# 2) с помощью генераторов и coroutine
# 3) с помощью синтаксиса async/await

