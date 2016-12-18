def isTriangleValid(a,b,c):
    vals = [a,b,c]
    vals.sort()
    return vals[0] + vals[1] > vals[2]

with open("3.1.data", 'r') as triangleData:
    reading = True
    counter = 0
    while reading:
        line1 = map(lambda valStr: int(valStr), triangleData.readline().split())
        line2 = map(lambda valStr: int(valStr), triangleData.readline().split())
        line3 = map(lambda valStr: int(valStr), triangleData.readline().split())
        if line3:
            counter = counter + sum([isTriangleValid(line1[0], line2[0], line3[0]),
                isTriangleValid(line1[1], line2[1], line3[1]),
                isTriangleValid(line1[2], line2[2], line3[2])])
        else:
            reading = False
    print counter