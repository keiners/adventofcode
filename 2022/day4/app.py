def run1():
    f = open("day4/input.txt", "r")
    lines = [line.strip() for line in f.readlines()]
    sum = 0
    for line in lines:
        foo = line.split(",")
        elf1 = [int(x) for x in foo[0].split("-")]
        elf2 = [int(x) for x in foo[1].split("-")]
        if (elf1[0] <= elf2[0]) and (elf1[1] >= elf2[1]):
            sum += 1
        elif (elf2[0] <= elf1[0]) and (elf2[1] >= elf1[1]):
            sum += 1
    print("Answer part 1: " + str(sum))

def run2():
    f = open("day4/input.txt", "r")
    lines = [line.strip() for line in f.readlines()]
    sum = 0
    for line in lines:
        foo = line.split(",")
        min1,max1 = (int(x) for x in foo[0].split("-"))
        min2,max2 = (int(x) for x in foo[1].split("-"))
        range1 = [x for x in range(min1, max1+1)]
        range2 = [x for x in range(min2, max2+1)]
        inCommon = list(set(range1) & set(range2))
        if len(inCommon) > 0:
            sum += 1
    print("Answer part 2: " + str(sum))

run1()
run2()