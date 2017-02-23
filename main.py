import numpy
def readOneLine():
    return list(map(lambda x: int(x) ,f.readline().replace('\n', '').split(' ')))

f = open('./kittens.in')



firstLineData = readOneLine()

V = firstLineData[0]
print "V = " + str(V)
E = firstLineData[1]
print "E = " + str(E)
R = firstLineData[2]
print "R = " + str(R)
C = firstLineData[3]
print "C = " + str(C)
X = firstLineData[4]
print "X = " + str(X)

S = readOneLine

L = []
K = []

CL = {}



for i in range(0, E - 1):
    line = readOneLine()

    L.append(line[0])
    K.append(line[1])

    for j in range(0, K[i] - 1):
        data = readOneLine()
        CL[i,data[0]] = data[1]

REQ = []
for q  in range(0, R - 1):
    REQ.append(readOneLine())

f.close()