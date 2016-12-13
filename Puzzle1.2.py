directionTurnLookup = {
    "N":{"R" : "E", "L": "W"},
    "E":{"R" : "S", "L": "N"},
    "S":{"R" : "W", "L": "E"},
    "W":{"R" : "N", "L": "S"}}

def incrementNorth(pos):
    return (pos[0], pos[1] + 1, 'N')

def incrementEast(pos):
    return (pos[0] + 1, pos[1], 'E')

def incrementSouth(pos):
    return (pos[0], pos[1] - 1, 'S')

def incrementWest(pos):
    return (pos[0] - 1, pos[1], 'W')

incrementForDirection = {
    "N": lambda pos: (pos[0], pos[1] + 1),
    "E": lambda pos: (pos[0] + 1, pos[1]),
    "S": lambda pos: (pos[0], pos[1] - 1),
    "W": lambda pos: (pos[0] - 1, pos[1])}

def testInputString(string):
    grid = {0:[0]}
    pos = (0, 0)
    currDir = "N"

    instructions = string.split(', ')
    for instruction in instructions:
        # decompose instuction
        turn = instruction[0]
        distance = int(instruction[1:])
        # updateDirection
        currDir = directionTurnLookup[currDir][turn]
        # update positions
        incrFn = incrementForDirection[currDir]
        for steps in range(0, distance):
            pos = incrFn(pos)
            if pos[0] in grid:
                if pos[1] in grid[pos[0]]:
                    return pos
                else:
                    grid[pos[0]].append(pos[1])
            else:
                grid[pos[0]] = [pos[1]]
    print 'Paths Never Cross'

test = "L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4"
print sum(map(abs, testInputString(test)))