class Ivan:
    def __call__(self, *args, **kwargs):
        print("__call__ called")

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")


i = Ivan()
i()
object