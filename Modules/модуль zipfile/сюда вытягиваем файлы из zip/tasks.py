from celery import Celery

app = Celery('tasks', broker='amqp://')


@app.task(ignore_result=True)
def print_hello():
    print('hello there')


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x + 1):
        if i not in multiples:
            results.append(i)
            for j in range(i * i, x + 1, i):
                multiples.append(j)
    return results
