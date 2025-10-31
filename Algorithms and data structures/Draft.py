from typing import List
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class DuplicatedItem:
    idx: int
    called_count: int = 0


# my solution
class Solution:
    def __init__(self, nums: List[int]):
        self.val_indexes = defaultdict(list)
        for idx, val in enumerate(nums):
            self.val_indexes[val].append(DuplicatedItem(idx))

    def pick(self, target: int) -> int:
        items = self.val_indexes[target]
        if len(items) == 1:
            return items[0].idx

        item = min(items, key=lambda x: x.called_count)
        item.called_count += 1
        return item.idx


# ChatGPT solution
import random


class Solution:

    def __init__(self, nums):
        self.indices = {}
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)

    def pick(self, target):
        return random.choice(self.indices[target])
