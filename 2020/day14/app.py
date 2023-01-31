import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day14/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    return (a1, a2)

def part1(lines):
    mask = ""
    memory = {}
    for line in lines:
        a,b = line.split(" = ")
        if a == "mask":
            mask = b
        elif a.startswith("mem"):
            m = int(re.findall("\d+", a)[0])
            n = int(b)
            bin_n = format(n, '036b')
            masked_n = mask_number(bin_n, mask)
            memory[m] = int(masked_n,2)
    return sum(memory.values())

def mask_number(number, mask):
    masked_number = ""
    for i,m in enumerate(mask):
        if m == "0" or m == "1":
            masked_number += m
        else:
            masked_number += number[i]
    return masked_number
    
def part2(lines):
    mask = ""
    memory = {}
    for line in lines:
        a,b = line.split(" = ")
        if a == "mask":
            mask = b
        elif a.startswith("mem"):
            m = int(re.findall("\d+", a)[0])
            n = int(b)
            bin_m = format(m, '036b')
            mem_masks = mask_number_with_float(bin_m, mask)
            for mem in mem_masks:
                memory[mem] = n
                
    return sum(memory.values())

def mask_number_with_float(number, mask):
    masked_number = ""
    for i,m in enumerate(mask):
        if m == "0":
            masked_number += number[i]
        elif m == "1":
            masked_number += "1"
        else:
            masked_number += "x"
    return float_number(masked_number)

def float_number(number):
    numbers = []
    if "x" not in number:
        return [number]
    else:
        x = number.index("x")
        prefix = number[:x]
        numbers += float_number(f"{prefix}0{number[x+1:]}")
        numbers += float_number(f"{prefix}1{number[x+1:]}")
    return numbers

assert run(True) == (51, 208), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
