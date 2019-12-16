from puzzle2 import OperationInfo, IntcodeComputer, Routine

@Routine(opcode=3, parameterCount=1)
def inputRoutine(opi: OperationInfo):
    opi[0] = opi.pc.input.pop(0)


@Routine(opcode=4, parameterCount=1)
def outputRoutine(opi: OperationInfo):
    opi.pc.output.append(opi[0])


def solve_part_1(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    pc = IntcodeComputer()
    pc.addRoutine(inputRoutine())
    pc.addRoutine(outputRoutine())

    pc.input = [1]
    pc.output = list()
    pc.execute(memory)
    return pc.output[-1]
