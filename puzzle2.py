def solve_part_1(puzzle_input: str):
    codes = [ int(val) for val in puzzle_input.split(',') ]
    codes[1], codes[2] = 12, 2
    i = 0
    while i < len(codes):
        op = codes[i]
        if op == 1:  # Add
            codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
            #log(codes)
        elif op == 2:  # Mult     
            codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
            #log(codes)
        elif op == 99:  # Terminate
            #log(codes)
            return codes[0]
        i += 4
