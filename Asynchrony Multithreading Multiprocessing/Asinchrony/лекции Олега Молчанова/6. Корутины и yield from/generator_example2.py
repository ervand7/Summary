def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


g = subgen()
print(g.send(None))  # Ready to accept message
print(g.send('Ok'))
"""
Traceback (most recent call last):
    print(g.send('Ok'))
StopIteration
"""
"""
В таком случае выполнение генератора осуществляется как бы уголком:
1) сначало выполнилось все, что до строчки с <yield> и сам <yield x>
поэтому когда мы вызвали метод send и передали туда None, мы получили это:
def subgen():
    x = 'Ready to accept message'
            = yield x

2) при втором вызове метода send мы получили то, что передали в метод send (это было 'Ok')
Это значение ('Ok') было записано переменная message. И мы в принте этот message увидели
    message 
    print('Subgen received:', message)
"""