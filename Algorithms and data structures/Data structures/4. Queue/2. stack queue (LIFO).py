# Создаем пустой список, который будет использоваться как очередь типа stack
my_stack_queue = []

# Добавляем элементы в "очередь"
my_stack_queue.append(1)
my_stack_queue.append(2)
my_stack_queue.append(3)

# Извлекаем элементы из "очереди" в порядке, обратном добавлению (Last-In-First-Out)
while my_stack_queue:
    item = my_stack_queue.pop()
    print("Извлечено из очереди типа stack:", item)
