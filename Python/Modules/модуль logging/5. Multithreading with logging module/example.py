import logging
import threading

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - [%(threadName)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)
logger = logging.getLogger(__name__)


def worker():
    for i in range(5):
        logger.info(f"log message {i} from worker thread")


thread = threading.Thread(target=worker)
thread.start()

for i in range(5):
    logger.info(f"log message {i} from main thread")

thread.join()

# 2022-08-30 18:14:03,011 - [INFO] - [Thread-1] - __main__ - (example.py).worker(13) - log message 0 from worker thread
# 2022-08-30 18:14:03,013 - [INFO] - [Thread-1] - __main__ - (example.py).worker(13) - log message 1 from worker thread
# 2022-08-30 18:14:03,013 - [INFO] - [Thread-1] - __main__ - (example.py).worker(13) - log message 2 from worker thread
# 2022-08-30 18:14:03,013 - [INFO] - [Thread-1] - __main__ - (example.py).worker(13) - log message 3 from worker thread
# 2022-08-30 18:14:03,013 - [INFO] - [Thread-1] - __main__ - (example.py).worker(13) - log message 4 from worker thread
# 2022-08-30 18:14:03,013 - [INFO] - [MainThread] - __main__ - (example.py).<module>(20) - log message 0 from main thread
# 2022-08-30 18:14:03,013 - [INFO] - [MainThread] - __main__ - (example.py).<module>(20) - log message 1 from main thread
# 2022-08-30 18:14:03,013 - [INFO] - [MainThread] - __main__ - (example.py).<module>(20) - log message 2 from main thread
# 2022-08-30 18:14:03,013 - [INFO] - [MainThread] - __main__ - (example.py).<module>(20) - log message 3 from main thread
# 2022-08-30 18:14:03,013 - [INFO] - [MainThread] - __main__ - (example.py).<module>(20) - log message 4 from main thread
