import package1
import app_logger

logger = app_logger.get_logger(__name__)


def main():
    logger.info("Программа стартует")
    package1.process(msg="сообщение")
    logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    logger.info("Программа завершила работу")


if __name__ == "__main__":
    main()

"""
2022-08-30 08:20:05,718 - [INFO] - __main__ - (main.py).main(8) - Программа стартует
2022-08-30 08:20:05,718 - [INFO] - package1 - (package1.py).process(7) - Перед процессом
2022-08-30 08:20:05,718 - [INFO] - package1 - (package1.py).process(9) - После процесса
2022-08-30 08:20:05,718 - [WARNING] - __main__ - (main.py).main(10) - Это должно появиться как в консоли, так и в файле журнала
2022-08-30 08:20:05,718 - [INFO] - __main__ - (main.py).main(11) - Программа завершила работу
сообщение
"""