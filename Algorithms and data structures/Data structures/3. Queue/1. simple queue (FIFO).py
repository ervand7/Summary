import queue

# Создаем пустую очередь
my_queue = queue.Queue()

# Добавляем элементы в очередь
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)

# Извлекаем элементы из очереди в порядке добавления (FIFO)
while not my_queue.empty():
    item = my_queue.get()
    print("Извлечено из очереди:", item)

# После извлечения все элементы очереди удалены
