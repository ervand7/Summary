"""
__eq__ (equal) отвечает за ==
__ne__ (not equal) отвечает за !=
__lt__ (less than) отвечает за <
__le__ (less equal) отвечает за <=
__gt__ (greater than) отвечает за >
__ge__ (greater equal) отвечает за >=
"""


class Tracks:
    def __init__(self, duration):
        self.duration = duration

    def __eq__(self, other):
        if isinstance(other, Tracks):
            return self.duration == other.duration

    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __ne__(self, other):
        return self.duration != other.duration

    def __ge__(self, other):
        return self.duration >= other.duration


track1 = Tracks(12)
track2 = Tracks(14)
track3 = Tracks(12)

print(track1 == track3)  # True
print(track1 < track2)  # True
print(track3 <= track2)  # True
print(track3 != track2)  # True
print(track1 >= track3)  # True
