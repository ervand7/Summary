def main(value):
    def inner():
        print('hello, my friend', value)

    return inner


a = main('Ivan')
a()  # hello, my friend Ivan
