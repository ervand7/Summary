# Bridge — separate what you do from how you do it
# ❓ The problem
# You have:
# - abstractions (what the client uses)
# - implementations (how it’s done)
# And you don’t want a class explosion like:
# RemoteSamsungTV, RemoteSonyTV, AdvancedRemoteSamsungTV, …

# Implementation
class Device:
    def on(self): pass


class TV(Device):
    def on(self):
        print("TV on")


class Radio(Device):
    def on(self):
        print("Radio on")


# Abstraction
class Remote:
    def __init__(self, device: Device):
        self.device = device

    def turn_on(self):
        self.device.on()


# Client
tv = TV()
radio = Radio()

Remote(tv).turn_on()
Remote(radio).turn_on()
