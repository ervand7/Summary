# @property разрешены

class Ivan:
    __slots__ = 'height', 'weight'

    def __init__(self, value_1, value_2):
        self.height = value_1
        self.weight = value_2

    @property
    def height_weight_sum(self):
        return self.height + self.weight


ivan = Ivan(value_1=170, value_2=70)
print(ivan.height)  # 170
print(ivan.weight)  # 70
print(ivan.height_weight_sum)  # 240
