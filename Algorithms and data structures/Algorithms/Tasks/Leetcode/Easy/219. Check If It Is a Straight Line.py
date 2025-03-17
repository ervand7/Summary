# ChatGPT solution
def check_straight_line(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx, dy = x1 - x0, y1 - y0

    for x, y in coordinates[2:]:
        if dx * (y - y0) != dy * (x - x0):
            return False
    return True


check_straight_line([[0, 1], [1, 3], [-4, -7], [5, 11]])
