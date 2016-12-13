directionTurnLookup = {
    "N":{"R" : "E", "L": "W"},
    "E":{"R" : "S", "L": "N"},
    "S":{"R" : "W", "L": "E"},
    "W":{"R" : "N", "L": "S"}}

def updateNorth(dist, pos):
    return (pos[0], pos[1] + dist, 'N')

def updateEast(dist, pos):
    return (pos[0] + dist, pos[1], 'E')

def updateSouth(dist, pos):
    return (pos[0], pos[1] - dist, 'S')

def updateWest(dist, pos):
    return (pos[0] - dist, pos[1], 'W')

updateForDirection = {
    "N": updateNorth,
    "E": updateEast,
    "S": updateSouth,
    "W": updateWest}

def f(string):
    instructions = string.split(', ')
    pos = [0,0]
    currDir = "N"
    for instruction in instructions:
        pos[0], pos[1], currDir = g(instruction, pos, currDir)
    return pos

def g(dirString, pos, currDir):
    turn = dirString[0]
    distance = int(dirString[1:])
    return updateForDirection[directionTurnLookup[currDir][turn]](distance, pos)

test = "L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4"
print sum(map(abs, f(test)))