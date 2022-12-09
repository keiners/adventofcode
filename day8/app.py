def run(test=False):
    fileName = "day8/test_input.txt" if test else "day8/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    trees = []
    for line in lines:
        treeLine = [tree for tree in line]
        trees.append(treeLine)
    visibleTrees = getVisibleTrees(trees)
    maxScore = getMaxScenicScore(trees)
    print("Visible Trees: "+str(visibleTrees))
    print("Max Scenic Score: "+str(maxScore))
    return (visibleTrees, maxScore)

def getVisibleTrees(trees):
    xLength = len(trees[0])
    yLength = len(trees)
    visibleTrees = 0
    for x in range(xLength):
        for y in range(yLength):
            if x == 0 or y == 0 or x == xLength-1 or y == yLength-1:
                visibleTrees += 1
            elif isVisible(x, trees[y]):
                visibleTrees += 1
            elif isVisible(y, getVerticalTreeLine(x, trees)):
                visibleTrees += 1
    return visibleTrees
    
def getMaxScenicScore(trees):
    xLength = len(trees[0])
    yLength = len(trees)
    maxScore = 0
    for x in range(xLength):
        for y in range(yLength):
            if x == 0 or y == 0 or x == xLength-1 or y == yLength-1:
                continue
            else:
                scoreX = getScenicScore(x, trees[y])
                scoreY = getScenicScore(y, getVerticalTreeLine(x, trees))
                if scoreX * scoreY > maxScore:
                    maxScore = scoreX * scoreY
    return maxScore

def getVerticalTreeLine(xPos, trees):
    return [trees[y][xPos] for y in range(len(trees))]

def isVisible(position, treeLine):
    treeHeight = treeLine[position]
    maxLeft = max(treeLine[:position])
    maxRight = max(treeLine[position + 1:])
    return (treeHeight > maxLeft or treeHeight > maxRight)

def getScenicScore(position, treeLine):
    treeHeight = treeLine[position]
    scoreLeft = 0
    scoreRight = 0
    for tree in reversed(treeLine[:position]):
        if tree >= treeHeight:
            scoreLeft += 1
            break
        else:
            scoreLeft += 1
    for tree in treeLine[position + 1:]:
        if tree >= treeHeight:
            scoreRight += 1
            break
        else:
            scoreRight += 1
    return scoreRight * scoreLeft
    
assert run(test=True) == (21, 8)
run()

