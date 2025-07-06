import random

bList = random.sample(range(1, 16), 5)
iList = random.sample(range(16, 31), 5)
nList = random.sample(range(31, 46), 5)
gList = random.sample(range(46, 61), 5)
oList = random.sample(range(61, 76), 5)

def bottomTopLine():
    print("*   *   *   *   *   *   *   *   *   *   *")

def printBingoLineLess(count, bList, iList, nList, gList, oList):
    print("*   " + str(bList[count]) + "   *   " + str(iList[count]) + "  *   " + str(nList[count]) + "  *   " + str(gList[count]) + "  *   " + str(oList[count]) + "  *")

def printBingoLineMore(count, bList, iList, nList, gList, oList):
     print("*  " + str(bList[count]) + "   *   " + str(iList[count]) + "  *   " + str(nList[count]) + "  *   " + str(gList[count]) + "  *   " + str(oList[count]) + "  *")

def numberLine(bList, iList=None, nList=None, gList=None, oList=None):
    count = 0
    while(count < 5):
            if (bList[count] < 10):
                printBingoLineLess(count, bList, iList, nList, gList, oList)
            else:
                printBingoLineMore(count, bList, iList, nList, gList, oList)    
            count+= 1

bottomTopLine()

numberLine(bList, iList, nList, gList, oList)

bottomTopLine()
