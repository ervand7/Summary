# Abstract Factory — create families of related objects
# ❓ The problem
# You need to create multiple related objects that must work together,
# and you want to switch the whole family at once.
# Example:
# Windows family → WindowsButton + WindowsCheckbox
# Mac family → MacButton + MacCheckbox

# Abstract products
class Button:
    def render(self) -> str:
        pass


class Checkbox:
    def render(self) -> str:
        pass


# Concrete products
class WindowsButton(Button):
    def render(self) -> str:
        return "Windows Button"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Windows Checkbox"


class MacButton(Button):
    def render(self) -> str:
        return "Mac Button"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Mac Checkbox"


# Abstract factory
class UIFactory:
    def create_button(self) -> Button:
        pass

    def create_checkbox(self) -> Checkbox:
        pass


# Concrete factories
class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Client
def client_code(factory: UIFactory):
    print(factory.create_button().render())
    print(factory.create_checkbox().render())


client_code(WindowsFactory())
client_code(MacFactory())
