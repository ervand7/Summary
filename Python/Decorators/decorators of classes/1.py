# Better to use multiple inheritance than class decorator

from typing import Any


def add_logging(cls: object) -> Any:
    # Define a new class that inherits from the input class.
    class Inner(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            Inner.__name__ = cls.__name__
            Inner.__doc__ = cls.__doc__

            self.log = []

        def log_action(self, action):
            self.log.append(f"Performed action: {action}")

    return Inner


@add_logging
class Example:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


# Create an instance of the decorated class
instance = Example("Alice")

# Call methods and log actions
print(instance.greet())  # Hello, Alice!
instance.log_action("Greeted Alice")
print(instance.log)  # ['Performed action: Greeted Alice']

print(Example.__name__)  # Example
