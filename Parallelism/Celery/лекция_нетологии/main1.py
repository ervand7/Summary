"""Безрезультатное использование celery без get."""
from time import time

from tasks import hard_cpu_function

start = time()
results = [
    hard_cpu_function.delay(1, 4),
    hard_cpu_function.delay(2, 1),
    hard_cpu_function.delay(2, 2)
]

print(results)  # [<AsyncResult: d5d1b378-c313-4b67-8354-4b2e557d4745>, <AsyncResult: 2d829fa1-d6f6-4556-8dea-1bb2518bc626>, <AsyncResult: 1d0e6243-0c61-4a57-8ad8-fd312a149262>]
print(time() - start)  # 0.6443390846252441
