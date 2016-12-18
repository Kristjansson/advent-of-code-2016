def decryptLetter(letter, offset):
    if letter == '-':
        return ' '
    else:
        letterNum = ord(letter) - ord('a')
        return chr(((letterNum + offset) % 26) + ord('a'))

# test case
# print ''.join(map(lambda c: decryptLetter(c, 343 % 26), 'qzmt-zixmtkozy-ivhz'))


with open('4.2.data', 'r') as validRoomNames, open('decryptedRoomNames', 'w') as decryptedRoomNames:
    for line in validRoomNames:
        tokens = line.strip(' \n\t\r').split('-')
        name = '-'.join(tokens[0:-1])
        sectorID, checkSum = tokens[-1][0:-1].split("[")
        offset = int(sectorID) % 26
        decryptedRoomName = map(lambda c: decryptLetter(c, offset), name)
        decryptedRoomNames.write(''.join(decryptedRoomName) + ' - ' + sectorID + "\n")