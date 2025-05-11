# my solution
def is_path_crossing(path: str) -> bool:
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def tuple(self):
            return (self.x, self.y)

    visited = set()
    current_point = Point(0, 0)

    visited.add(current_point.tuple())
    for i in path:
        if i == "N":
            new_point = Point(x=current_point.x, y=current_point.y + 1)
        elif i == "E":
            new_point = Point(x=current_point.x + 1, y=current_point.y)
        elif i == "S":
            new_point = Point(x=current_point.x, y=current_point.y - 1)
        elif i == "W":
            new_point = Point(x=current_point.x - 1, y=current_point.y)

        if new_point.tuple() in visited:
            return True
        visited.add(new_point.tuple())
        current_point = new_point

    return False


print(is_path_crossing("SS"))


# ChatGPT solution
def is_path_crossing(path: str) -> bool:
    visited = set()
    x, y = 0, 0
    visited.add((x, y))  # Add starting point

    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False
