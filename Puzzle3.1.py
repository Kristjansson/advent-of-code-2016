def isTriangleValid(a,b,c):
    vals = [a,b,c]
    vals.sort()
    return vals[0] + vals[1] > vals[2]

with open("3.1.data", 'r') as triangleData:
    print len([line for line in triangleData if isTriangleValid(*map(lambda valStr: int(valStr), line.split()))])