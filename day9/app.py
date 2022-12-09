def run(knots, test=False):
    fileName = "day9/test_input.txt" if test else "day9/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    knotPositions = [(0,0) for x in range(knots)]
    tailPositions = [knotPositions[-1]]
    for line in lines:
        direction, steps = line.split()
        for i in range(int(steps)):
            knotPositions[0] = moveHead(knotPositions[0], direction)
            for i in range(knots - 1):
                head = knotPositions[i]
                tail = knotPositions[i+1]
                if not isAdjacent(head, tail):
                    knotPositions[i+1] = moveTail(head, tail)
                else: break
            tailPositions.append(knotPositions[-1])
    lenTailPositions = len(set(tailPositions))
    return lenTailPositions
    
def moveHead(oldPos, direction):
    if direction == "R":
        return (oldPos[0]+1, oldPos[1])
    elif direction == "L":
        return (oldPos[0]-1, oldPos[1])
    elif direction == "U":
        return (oldPos[0], oldPos[1]+1)
    elif direction == "D":
        return (oldPos[0], oldPos[1]-1)
    
def moveTail(headPos, tailPos):
    xPos = tailPos[0]
    yPos = tailPos[1]
    if tailPos[0] == headPos[0]:
        if tailPos[1] > headPos[1]:
            yPos -= 1
        else:
            yPos += 1
    elif tailPos[1] == headPos[1]:
        if tailPos[0] > headPos[0]:
            xPos -= 1
        else:
            xPos += 1
    else:
        if tailPos[0] > headPos[0]:
            xPos -= 1
        else:
            xPos += 1
        if tailPos[1] > headPos[1]:
            yPos -= 1
        else:
            yPos += 1
    return (xPos, yPos)
        
def isAdjacent(posH, posT):
    diffX = abs(posH[0] - posT[0])
    diffY = abs(posH[1] - posT[1])
    if diffX <= 1 and diffY <= 1:
        return True
    else: 
        return False
    
assert run(2, test=True) == 13
assert run(10, test=True) == 1
answer1 = run(2)
print("Part 1: Tail Positions: " + str(answer1))
answer2 = run(10)
print("Part 2: Tail Positions: " + str(answer2))
