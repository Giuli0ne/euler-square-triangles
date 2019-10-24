perimeter = 120

def findThirdSide(a,b):
    return perimeter - a - b

def isRectangle(a,b,c):
    return a**2 + b**2 == c**2

def findSolutions(per):
    solList = []
    for i in range(1,per):
        for j in range(i,per):
            k = findThirdSide(i,j)
            if isRectangle(i,j,k):
                solList.append((i,j,k))
    return solList

def countSolution(solutionList):
    msg =  "{} soluzioni"
    num = len(solutionList)
    print("OK")
    print(msg.format(num)

def printSolution(solutionList):
    for el in solutionList:
        msg = "({},{},{})"
        print(msg.format(el[0],el[1],el[2]))

for i in range(1,1000):
    countSolution(findSolutions(i))
