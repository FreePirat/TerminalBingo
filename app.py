import random

bList = [random.randint(1, 15) for num in range(5)]
iList = [random.randint(16, 30) for num in range(5)]
nList = [random.randint(31, 45) for num in range(5)]
gList = [random.randint(46, 60) for num in range(5)]
oList = [random.randint(61, 75) for num in range(5)]

def bottomTopLine():
    count = 0
    line = ""
    while(count < 5):
        line += "*   *   *   *   *   "
        count += 1
    print(line)

def numberLine(listOfNums):
    count = 0
    line = ""
    while(count < 5):
        line += "*   " + str(listOfNums[count]) + "   "
        count+= 1
    print(line)





bottomTopLine()

numberLine(bList)



bottomTopLine()
