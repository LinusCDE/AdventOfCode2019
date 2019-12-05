def hasDecrease(digits):
    lastDigit = digits[0]
    for digit in digits[1:]:
        if lastDigit > digit:
            return True
        lastDigit = digit
    return False


def hasPair(digits):
    lastDigit = digits[0]
    for digit in digits[1:]:
        if lastDigit == digit:
            return True
        lastDigit = digit
    return False


def generateDigits(firstGuess, lastGuess):
    # Python generator hell xD
    return ( tuple(map(int, digitsStr)) for digitsStr in map(str, range(firstGuess, lastGuess+1)) )

def solve_part_1(puzzle_input: str):
    validGuesses = 0
    for guessDigits in generateDigits(*map(int, puzzle_input.split('-'))):
        if not hasDecrease(guessDigits) and hasPair(guessDigits):
            validGuesses += 1

    return validGuesses


def hasStrictPair(digits):
    digits = -1, *digits, -1  # Pad -1 left and right
    for digit1, digit2, digit3, digit4 in zip(digits[:-3], digits[1:-2], digits[2:-1], digits[3:]):
        if digit1 != digit2 and digit2 == digit3 and digit3 != digit4:
            return True
    return False


def solve_part_2(puzzle_input: str):
    validGuesses = 0
    for guessDigits in generateDigits(*map(int, puzzle_input.split('-'))):
        if not hasDecrease(guessDigits) and hasStrictPair(guessDigits):
            validGuesses += 1
    return validGuesses

