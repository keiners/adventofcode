def runPart1():
    f = open("day1/input.txt", "r")
    lines = f.readlines()
    lines.append("\n")
    maxCal = 0
    currentCal = 0
    for line in lines:
        if line != "\n":
            currentCal += int(line)
        else:
            if currentCal > maxCal:
                maxCal = currentCal
            currentCal = 0
    print("Part 1 answer: "+str(maxCal))
    
def runPart2():
    f = open("day1/input.txt", "r")
    lines = f.readlines()
    lines.append("\n")
    currentCal = 0
    listOfCal = []
    for line in lines:
        if line != "\n":
            currentCal += int(line)
        else:
            listOfCal.append(currentCal)
            currentCal = 0
    listOfCal.sort(reverse=True)
    print("Part 2 answer: "+str(listOfCal[0]+listOfCal[1]+listOfCal[2]))
    
runPart1()
runPart2()