from coordinate_utils import CoordinateField, add


def distance(pos1: tuple, pos2: tuple):
    '''Returns the Manhattan distance of two points.'''
    # Scheme: n_dist = (p1N - p2N) if (p1N > p2N) else (p2N - p1N)
    x_dist = pos1[0] - pos2[0] if pos1[0] > pos2[0] else pos2[0] - pos1[0]
    y_dist = pos1[1] - pos2[1] if pos1[1] > pos2[1] else pos2[1] - pos1[1]
    return x_dist + y_dist

DIRECTIONS = {
    'U': ( 0,  1),  # Up
    'D': ( 0, -1),  # Down
    'L': (-1,  0),  # Left
    'R': ( 1,  0),  # Right
}

def solve_part_1(puzzle_input: str):
    field = CoordinateField()
    
    wireNum = 0
    for wire in puzzle_input.split('\n'):
        wireNum += 1
        pos = (0, 0)
        for instruction in wire.split(','):
            directionVector = DIRECTIONS[instruction[0]]
            count = int(instruction[1:])
            for _ in range(count):
                pos = add(pos, directionVector)
                field[pos] = field.get(pos, default=0) + wireNum

    # Fields with wire 1 have value of 1
    # Fields with wire 2 have value of 2
    # Fields with both wires have value of > 2

    closestDist = None
    for x, y, value in field.items():
        if value == 3 and not (x == 0 and y == 0):
            # Using value of 3 will most likely (not guaranteed)
            # only yield positions with two different wires crossing.
            # More don't seem to count.
            dist = distance((0,0), (x,y))
            log(x,y,value,dist)
            if closestDist is None or dist < closestDist:
                closestDist = dist
    return closestDist
