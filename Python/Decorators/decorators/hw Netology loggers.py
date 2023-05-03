from datetime import date, datetime
import os
from functools import wraps


# variant with built way
def decorator_logger(func):
    file_path = os.path.join(os.getcwd(), 'super_log.log')

    @wraps(func)
    def inner(*args, **kwargs):
        with open(file_path, mode='a+', encoding='utf8') as log_file:
            start = datetime.now()
            log_file.write(f'Function "{func.__name__}" started at {date.today()} {datetime.now().time()}\n')
            log_file.write(f'*args is: {args}\n**kwargs is: {kwargs}\n')
            result_of_func = func(*args, **kwargs)
            log_file.write(f'Result is: {result_of_func}\n')
            end = datetime.now() - start
            log_file.write(f'Function performed duration is: {end}\n')
            log_file.write(f'Documentation: {func.__doc__}\n\n')
        return result_of_func

    return inner


# variant where user can write filename in parameter to current decorator
def decorator_with_way_to_file(file_name='super_log.log'):
    def my_decorator_logger(func):
        file_path = os.path.join(os.getcwd(), file_name)

        @wraps(func)
        def inner(*args, **kwargs):
            with open(file_path, mode='a+', encoding='utf8') as log_file:
                start = datetime.now()
                log_file.write(f'Function "{func.__name__}" started at {date.today()} {datetime.now().time()}\n')
                log_file.write(f'*args is: {args}\n**kwargs is: {kwargs}\n')
                result_of_func = func(*args, **kwargs)
                log_file.write(f'Result is: {result_of_func}\n')
                end = datetime.now() - start
                log_file.write(f'Function performed duration is: {end}\n')
                log_file.write(f'Documentation: {func.__doc__}\n\n')
            return result_of_func

        return inner

    return my_decorator_logger
