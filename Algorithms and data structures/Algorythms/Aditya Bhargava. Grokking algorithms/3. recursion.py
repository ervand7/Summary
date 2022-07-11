def countdown(i):
    print(i)
    if i <= 1:
        return
    countdown(i - 1)


countdown(55)
