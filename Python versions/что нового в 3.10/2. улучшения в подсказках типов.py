"""
# Намеренно забудем закрывающую скобку:
print('Hello world'

# получим хорошую подсказку в трейсбеке
print('Hello world'
         ^
SyntaxError: '(' was never closed
"""
