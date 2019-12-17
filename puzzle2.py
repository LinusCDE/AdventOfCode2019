from itertools import permutations
from abc import ABC, abstractmethod


class OperationInfo:
    '''
    Provides information about the current operation
    and is subscriptable for parameter access which respects
    the respective parameter modes.
    '''
    MODE_POSITION = 0 # Pointer-ish
    MODE_IMMEDIATE = 1 # Direct
    def __init__(self, pc: 'IntcodeComputer', memory: list, opCodeIndex: int, parameterCount: int):
        self.pc = pc
        self.memory = memory
        self.opcodeIndex = opCodeIndex
        self.parameterCount = parameterCount
        fullOpInfo = str(memory[opCodeIndex]).zfill(2 + parameterCount)
        self.opcode = int(fullOpInfo[-2:]) # Last two chars as int
        self.modes = [ int(mode) for mode in fullOpInfo[:-2][::-1] ]
        self.postExecutionCustomIp = None

    def __getitem__(self, parameterIndex: int):
        mode = self.modes[parameterIndex]
        i = self.opcodeIndex + 1 + parameterIndex
        if mode == OperationInfo.MODE_POSITION:
            return self.memory[self.memory[i]]
        elif mode == OperationInfo.MODE_IMMEDIATE:
            return self.memory[i]
        else:
            raise RuntimeError('Invalid mode on reading: %s (rawop: %d)' % (mode, self.memory[self.opcodeIndex]))

    def __setitem__(self, parameterIndex: int, value: int):
        mode = self.modes[parameterIndex]
        i = self.opcodeIndex + 1 + parameterIndex
        if mode == OperationInfo.MODE_POSITION:
            self.memory[self.memory[i]] = value
        elif mode == OperationInfo.MODE_IMMEDIATE:
            self.memory[i] = value
        else:
            raise RuntimeError('Invalid mode on writing: %s (rawop: %d)' % (mode, self.memory[self.opcodeIndex]))


class IntcodeRoutine(ABC):
    opcode = None
    parameterCount = None

    @abstractmethod
    def run(self, operationInfo: OperationInfo):
        pass


def Routine(opcode: int, parameterCount: int):
    '''
    Decorator that generates a instantiable class
    based on IntcodeRoutineClass with to run the method as run
    '''
    def decorator(func):
        def wrapper():
            routineClass = type(func.__name__, (IntcodeRoutine,), {
                'opcode': opcode,
                'parameterCount': parameterCount,
                'run': lambda *args, **kwargs: func(*args, **kwargs)
                })
            return routineClass
        return wrapper
    return decorator


class IntcodeComputer:

    def __init__(self):
        self.routines = dict()
        self.addDefaultRoutines()

    def addDefaultRoutines(self):
        self.addRoutine(AdditionRoutine())
        self.addRoutine(MultiplicationRoutine())

    def addRoutine(self, routine: IntcodeRoutine):
        self.routines[routine.opcode] = routine

    def execute(self, mem, noun=None, verb=None) -> int:
        # Initialize copy of memory
        mem = list(mem)
        if verb is not None and noun is not None:
            mem[1], mem[2] = noun, verb

        # Execute program
        ip = 0  # ip = instruction pointer
        while ip < len(mem):
            opcode = mem[ip]
            if opcode == 99:
                return mem[0]
            else:
                routine = self.routines[int(str(opcode).zfill(2)[-2:])]
                opi = OperationInfo(self, mem, ip, routine.parameterCount)
                routine.run(opi)
                
                if opi.postExecutionCustomIp is not None:
                    ip = opi.postExecutionCustomIp
                else:
                    ip += 1 + routine.parameterCount


@Routine(opcode=1, parameterCount=3)
def AdditionRoutine(opi: OperationInfo):
    opi[2] = opi[0] + opi[1]


@Routine(opcode=2, parameterCount=3)
def MultiplicationRoutine(opi: OperationInfo):
    opi[2] = opi[0] * opi[1]


def solve_part_1(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    return IntcodeComputer().execute(memory, 12, 2)


def solve_part_2(puzzle_input: str):
    memory = tuple( map(int, puzzle_input.split(',')) )
    computer = IntcodeComputer()
    for noun, verb in permutations(tuple(range(0, 100)), 2):
        result = computer.execute(memory, noun, verb)
        if result == 19690720:
            return 100 * noun + verb
