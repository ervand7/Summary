from headers import header


class Message(object):

    def __init__(self):
        super().__init__()

        self.blank = None

    @property
    def text(self):
        return self.blank

    @text.setter
    def text(self, value):
        del self.text
        self.blank = header
        self.blank = self.blank.format(**value)

    @text.deleter
    def text(self):
        self.blank = None


msg = Message()
