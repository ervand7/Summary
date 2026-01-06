# Command — turn a request into an object
# ❓ The idea
# Encapsulate an action as an object so it can be passed, stored, or executed later.

# Command interface
class Command:
    def execute(self):
        pass


# Receiver
class Light:
    def on(self):
        print("Light is ON")


# Concrete command
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


# Invoker
class Button:
    def __init__(self, command: Command):
        self.command = command

    def press(self):
        self.command.execute()


# Usage
light = Light()
command = LightOnCommand(light)
button = Button(command)

button.press()
