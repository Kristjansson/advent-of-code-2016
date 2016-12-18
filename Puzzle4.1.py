from collections import Counter

with open('4.data') as encryptedRoomNames, open('4.2.data', 'w') as validRoomNames:
    sectorIDSum = 0
    for line in encryptedRoomNames:
        tokens = line.strip(' \n\t\r').split('-')
        name = ''.join(tokens[0:-1])
        sectorID, checkSum = tokens[-1][0:-1].split("[")
        if ''.join([pair[0] for pair in sorted(Counter(name).most_common(), key=lambda x: (-x[1], x[0]))][0:5]) == checkSum:
            sectorIDSum = sectorIDSum + int(sectorID)
            validRoomNames.write(line)
print sectorIDSum