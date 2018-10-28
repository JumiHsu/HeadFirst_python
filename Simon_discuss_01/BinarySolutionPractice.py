Data = [5,2,3,4,3,4]

def SolutionA(A):
    tempN = 0
    for i in range(len(A)):
        tempN += pow(2,A[i])
    #print(tempN)
    return tempN

def FindNearestBinarySolution(B):
    num = 0
    while pow(2,num) <= B:
        num += 1
    return num-1

def GetBinarySquareSolution(ARR):
    finalnum = 0
    for i in range(len(ARR)):
        finalnum += pow(2,ARR[i])
    #print(finalnum)
    return finalnum

nSol = SolutionA(Data)
print(nSol)
nTempSol = nSol
nNearest = FindNearestBinarySolution(nSol)
arrSol = [nNearest]
while nSol != GetBinarySquareSolution(arrSol):
    nTempSol -= pow(2,nNearest)
    nNearest = FindNearestBinarySolution(nTempSol)
    arrSol.append(nNearest)
print(arrSol)
print("End")