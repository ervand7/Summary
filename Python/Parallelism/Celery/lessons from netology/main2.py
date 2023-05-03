from time import time

from tasks import hard_cpu_function

start = time()
async_results = [
    hard_cpu_function.delay(1, 4),
    hard_cpu_function.delay(2, 1),
    hard_cpu_function.delay(2, 2)
]
results = []
for async_result in async_results:
    res = async_result.get()
    results.append(res)
print(results)  # [5, 3, 4]
print(time() - start)  # 6.629324197769165

"""
Почему именно 6 секунд:
celery был запущен в 2 процессах. Первые 2 отработали за 3 секунды.
А следующим на очереди отработал 3й (тоже 3 секунды).
Если запустим 3 процесса celery:
 ● celery -A tasks.app worker -c 3
то у нас все отработает за 3 секунды.
"""

