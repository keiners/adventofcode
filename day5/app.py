def run1():
    f = open("day5/input.txt", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    stacks = int((len(lines[0])+1)/4)
    containers = ["" for x in range(0,stacks)]
    setupComplete = False
    for line in lines:
        if len(line) == 0:
            setupComplete = True
        elif not setupComplete:
            indices = [x for x in range(1, len(line), 4)]
            counter = 0
            for i in indices:
                crate = line[i]
                if not crate.isnumeric() and not crate == " ":
                    containers[counter] += crate
                counter +=1
        else:
            orders = [int(line.split()[i]) for i in range(1,6,2)]
            for i in range(orders[0]):
                moveFrom = orders[1]-1
                moveTo = orders[2]-1
                crate = containers[moveFrom][0]
                containers[moveFrom] = containers[moveFrom][1:]
                containers[moveTo] = crate + containers[moveTo]
    result = ""
    for i in range(stacks):
        result += containers[i][0]
    print("Answer part 1: " + result)
        
def run2():
    f = open("day5/input.txt", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    stacks = int((len(lines[0])+1)/4)
    containers = ["" for x in range(0,stacks)]
    setupComplete = False
    for line in lines:
        if len(line) == 0:
            setupComplete = True
        elif not setupComplete:
            indices = [x for x in range(1, len(line), 4)]
            counter = 0
            for i in indices:
                crate = line[i]
                if not crate.isnumeric() and not crate == " ":
                    containers[counter] += crate
                counter +=1
        else:
            orders = [int(line.split()[i]) for i in range(1,6,2)]
            moveAmount = orders[0]
            moveFrom = orders[1]-1
            moveTo = orders[2]-1
            crate = containers[moveFrom][0:moveAmount]
            containers[moveFrom] = containers[moveFrom][moveAmount:]
            containers[moveTo] = crate + containers[moveTo]
    result = ""
    for i in range(stacks):
        result += containers[i][0]
    print("Answer part 2: " + result)
    
run1()
run2()