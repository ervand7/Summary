class B1:
    pass


class B2:
    pass


newClass = type(
    'Point',
    (B1, B2),
    {'MAX_COORD': 100, 'MIN_COORD': 0}
)

print(newClass.__dict__)  # {'MAX_COORD': 100, 'MIN_COORD': 0, '__module__': '__main__', '__doc__': None}
print(newClass.__mro__)  # (<class '__main__.Point'>, <class '__main__.B1'>, <class '__main__.B2'>, <class 'object'>)
