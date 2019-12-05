from itertools import permutations

def execute(mem, noun, verb):
    # Initialize copy of memory
    mem = list(mem)
    mem[1], mem[2] = noun, verb

    # Execute program
    instructionPtr = 0
    for ip in range(0, len(mem), 4):  # ip = instruction pointer
        opcode = mem[ip]
        if opcode == 1:  # Add
            mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
            #log(codes)
        elif opcode == 2:  # Mult     
            mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
            #log(codes)
        elif opcode == 99:  # Terminate
            #log(codes)
            return mem[0]


def solve_part_1(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    return execute(memory, 12, 2)

def solve_part_2(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    for noun, verb in permutations(tuple(range(0, 100)), 2):
        result = execute(memory, noun, verb)
        if result == 19690720:
            return 100 * noun + verb
