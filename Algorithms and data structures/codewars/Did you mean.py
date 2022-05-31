import re
from itertools import chain, combinations
from typing import Iterable


class Dictionary:
    def __init__(self, words) -> None:
        self.words = words

    @staticmethod
    def find_combinations(data: list) -> list:
        result: chain = chain.from_iterable(
            combinations(data, i) for i in range(len(data) + 1)
        )
        result: list = [item for item in result if len(item) > 1]
        return result

    def find_most_similar(self, term: str) -> str:
        changes = 100
        closest_word = str()
        for word in self.words:
            if len(self.words) > len(term):
                longer = word
                shorter = term
            else:
                longer = term
                shorter = word
            letters_in_longer = [letter for letter in shorter if letter in longer]

            letters_combinations = self.find_combinations(letters_in_longer)
            for i in letters_combinations:  # type: tuple
                regex = str()
                for let in i:
                    regex += r'[A-Za-z]*' + re.escape(let)
                regex += r'[A-Za-z]*'
                if all([
                    re.search(regex, longer),
                    (len(longer) - len(i)) < changes]
                ):
                    changes = len(longer) - len(i)
                    closest_word = word
        return closest_word
