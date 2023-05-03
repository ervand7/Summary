"""В этом файле видно, как медленно отрабатывает приложение без celery."""
from time import sleep, time


def hard_cpu_function(a, b):
    sleep(3)
    return a + b


start = time()
results = [hard_cpu_function(1, 4), hard_cpu_function(2, 1), hard_cpu_function(2, 2)]
print(time() - start)  # 9.008142948150635


