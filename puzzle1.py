def solve_part_1(puzzle_input: str):
    fuelSum = 0
    for mass in map(int, puzzle_input.split('\n')):
        fuelSum += (mass // 3) - 2
    return fuelSum

def solve_part_2(puzzle_input: str):
    fuelSum = 0
    for mass in map(int, puzzle_input.split('\n')):
        fuel = mass
        while fuel > 0:
            fuel = (fuel // 3) - 2
            fuelSum += fuel if fuel > 0 else 0
    return fuelSum
