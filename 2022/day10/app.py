from textwrap import wrap

def run(test=False):
    fileName = "day10/test_input.txt" if test else "day10/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    cycle = 1
    value = 1
    cycleValues = {}
    for line in lines:
        instruction = line.split()
        if instruction[0] == "noop":
            cycleValues[cycle] = value
            cycle += 1
        elif instruction[0] == "addx":
            cycleValues[cycle] = value
            cycleValues[cycle+1] = value
            value += int(instruction[1])
            cycle += 2

    if not test: printCRT(cycleValues)
    sum = findSum([20, 60, 100, 140, 180, 220], cycleValues)
    return sum
    
def findSum(indexes, valueDict):
    sum = 0
    for i in indexes:
        sum += i * valueDict[i]
    return sum

def printCRT(dict):
    image = ""
    for k, v in dict.items():
        cycleIndex = (k-1) % 40
        if v-1 <= cycleIndex <= v+1:
            image += "#"
        else:
            image += "."

    imageLines = wrap(image, 40)
    for line in imageLines:
        print(line)

assert run(test=True) == 13140
print(run())