import logging
import multiprocessing
import os
from logging.handlers import QueueHandler

formatter = "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
logging.basicConfig(level=logging.INFO)


def log_processor(queue):
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("a.log")
    file_handler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(file_handler)

    while True:
        try:
            record = queue.get()
            if record is None:
                break
            logger.log(record.levelno, record.msg)
        except Exception as e:
            pass


def log_producer(queue):
    pid = os.getpid()
    logger = logging.getLogger(__name__)
    queue_handler = QueueHandler(queue)
    logger.addHandler(queue_handler)

    logger.info(f"info - producer {pid}")
    logger.warning(f"warning - producer {pid}")


def main():
    queue = multiprocessing.Queue(-1)
    listener = multiprocessing.Process(target=log_processor, args=(queue,))
    listener.start()
    workers = []
    for i in range(2):
        worker = multiprocessing.Process(target=log_producer, args=(queue,))
        workers.append(worker)
        worker.start()
    for w in workers:
        w.join()
    queue.put_nowait(None)
    listener.join()


if __name__ == '__main__':
    main()

# INFO:__mp_main__:info - producer 66208
# WARNING:__mp_main__:warning - producer 66208
# INFO:__mp_main__:info - producer 66208
# WARNING:__mp_main__:warning - producer 66208
# INFO:__mp_main__:info - producer 66209
# WARNING:__mp_main__:warning - producer 66209
# INFO:__mp_main__:info - producer 66209
# WARNING:__mp_main__:warning - producer 66209
