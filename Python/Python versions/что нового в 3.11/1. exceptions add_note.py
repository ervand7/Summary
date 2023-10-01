try:
    1/0
except ZeroDivisionError as err:
    err.add_note("Дополнительная заметка")
    print(err.__notes__)  # ['Дополнительная заметка']
    raise

# Traceback (most recent call last):
#   File "/Users/ervand_agadzhanyan/Desktop/Summary/Python/Python versions/что нового в 3.11/1. exceptions add_note.py", line 2, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero
# Дополнительная заметка