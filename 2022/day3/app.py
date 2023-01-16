import numpy as np

def run1():
    f = open("day3/input.txt", "r")
    lines = [line.strip() for line in f.readlines()]
    sum = 0
    for line in lines:
        items = [char for char in line]
        comps = np.array_split(items, 2)
        common = list(set(comps[0]) & set(comps[1]))
        sum += getPriority(common[0])
    print("Part 1. Sum of all priorities: " + str(sum))

def run2():
    f = open("day3/input.txt", "r")
    lines = [line.strip() for line in f.readlines()]
    sum = 0
    for x in range(0, len(lines), 3):
        elf1 = [char for char in lines[x]]
        elf2 = [char for char in lines[x+1]]
        elf3 = [char for char in lines[x+2]]
        common = list(set(elf1) & set(elf2) & set(elf3))
        sum += getPriority(common[0])
    print("Part 2. Sum of all priorities: " + str(sum))

def getPriority(letter):
    if str.islower(letter):
        return ord(letter) - 96
    else:
        return ord(letter) - 38

run1()
run2()