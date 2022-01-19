# 3.9
with open('file1.txt', 'r') as file1, \
        open('file2.txt', 'w') as file2:
    file2.write(file1.read())

# 3.10
"""
Почему-то не работает, а должно...
with (open('file1.txt', 'r') as file1,
      open('file2.txt', 'w') as file2):
    file2.write(file1.read())
"""