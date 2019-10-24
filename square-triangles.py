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
    msg =  "{} soluzioni per {}"
    return len(solutionList)
    #print(msg.format(num,i))

def printSolution(solutionList):
    for el in solutionList:
        msg = "({},{},{})"
        print(msg.format(el[0],el[1],el[2]))

maxCount = 0
for i in range(1,1001):
    maxCount = max(maxCount,countSolution(findSolutions(i)))
    print("Massimo numero di soluzioni: ",maxCount, "(", i,")", end="\r")
