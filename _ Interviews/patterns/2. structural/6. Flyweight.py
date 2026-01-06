# Flyweight — share objects to save memory
# ❓ The problem
# You have many similar objects, and creating each one separately wastes memory.
# Example:
# millions of characters in a text editor
# particles in a game
# map tiles, icons, glyphs

# Flyweight (shared, immutable)
class Character:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def draw(self, position: int):
        print(f"{self.symbol} at {position}")


# Flyweight factory
class CharacterFactory:
    _cache: dict[str, Character] = {}

    @classmethod
    def get(cls, symbol: str) -> Character:
        if symbol not in cls._cache:
            cls._cache[symbol] = Character(symbol)
        return cls._cache[symbol]


# Client
text = "hello"
for i, ch in enumerate(text):
    char = CharacterFactory.get(ch)
    char.draw(i)
