def run(test=False):
    fileName = "day13/test_input.txt" if test else "day13/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    counter = 0
    sum = 0
    for i in range(0, len(lines), 3):
        counter += 1
        left = eval(lines[i])
        right = eval(lines[i+1])
        comparison = compare(left, right)
        if comparison == 1:
            sum += counter
    print("Sum: "+str(sum))

def run2(test=False):
    fileName = "day13/test_input.txt" if test else "day13/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    pack1 = [[2]]
    pack1Index = 1
    pack2 = [[6]]
    pack2Index = 2
    for line in lines:
        if line == "":
            continue
        x = eval(line)
        comparison1 = compare(x, pack1)
        if comparison1 == 1:
            pack1Index += 1
        comparison2 = compare(x, pack2)
        if comparison2 == 1:
            pack2Index += 1
    print("Decoder key: "+str(pack1Index*pack2Index))
        
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compareInt(left, right)
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])
    elif left and right:
        comparison = compare(left[0], right[0])
        if comparison == 0:
            return compare(left[1:], right[1:])
        else:
            return comparison
    else:
        if right:
            return 1
        elif left:
            return -1
        else: return 0
    
def compareInt(left, right):
    if left == right:
        return 0
    elif left < right:
        return 1
    else: 
        return -1

run()
run2()