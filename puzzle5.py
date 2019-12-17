from puzzle2 import OperationInfo, IntcodeComputer, Routine

@Routine(opcode=3, parameterCount=1)
def InputRoutine(opi: OperationInfo):
    opi[0] = opi.pc.input.pop(0)


@Routine(opcode=4, parameterCount=1)
def OutputRoutine(opi: OperationInfo):
    opi.pc.output.append(opi[0])


def solve_part_1(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    pc = IntcodeComputer()
    pc.addRoutine(InputRoutine())
    pc.addRoutine(OutputRoutine())

    # Input and output are first declared here. Those are used
    # by the Input and Output Routines.
    pc.input = [1]
    pc.output = list()
    pc.execute(memory)
    return pc.output[-1]


@Routine(opcode=5, parameterCount=2)
def JumpIfTrueRoutine(opi: OperationInfo):
    if opi[0]:
        opi.postExecutionCustomIp = opi[1]


@Routine(opcode=6, parameterCount=2)
def JumpIfFalseRoutine(opi: OperationInfo):
    if not opi[0]:
        opi.postExecutionCustomIp = opi[1]


@Routine(opcode=7, parameterCount=3)
def JumpIfLessThanRoutine(opi: OperationInfo):
    opi[2] = opi[0] < opi[1]


@Routine(opcode=8, parameterCount=3)
def JumpIfEqualsRoutine(opi: OperationInfo):
    opi[2] = opi[0] == opi[1]


def solve_part_2(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    pc = IntcodeComputer()
    pc.addRoutine(InputRoutine())
    pc.addRoutine(OutputRoutine())
    pc.addRoutine(JumpIfTrueRoutine())
    pc.addRoutine(JumpIfFalseRoutine())
    pc.addRoutine(JumpIfLessThanRoutine())
    pc.addRoutine(JumpIfEqualsRoutine())

    # Input and output are first declared here. Those are used
    # by the Input and Output Routines.
    pc.input = [5]
    pc.output = list()
    pc.execute(memory)
    return pc.output[-1]
