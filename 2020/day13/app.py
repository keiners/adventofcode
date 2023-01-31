import re, math
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day13/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    start = int(lines[0])
    ids = [int(i) for i in re.findall("\d+", lines[1])]
    lowest_wait = 99999
    for i in ids:
        time_since_bus = start % i
        if i-time_since_bus < lowest_wait:
            lowest_wait = i-time_since_bus
            answer = i * lowest_wait
    return answer

def part2(lines):
    ids = lines[1].split(",")
    
    print(ids)
    max_id = max([int(i) for i in ids if i != "x"])
    max_i = ids.index(str(max_id))
    print(max_id)
    print(max_i)
    minute = 0
    #minute = 1068785
    while True:
        
        finished = True
        for i in [int(i) for i in ids if i != "x"]:
            index = ids.index(str(i))
            minute_for_bus = minute - (max_i - index)
            modulo = i
            if minute==1068785:
                print(f"{minute_for_bus} mod {modulo} is 0")
                print(f"{minute} mod {i} is {max_i-index}")
            if not minute_for_bus % modulo == 0:
            #if not minute % i == max_i-index:
                finished = False
                break
        if finished:
            print(minute)
            return minute-max_i
        minute += max_id

assert run(True) == (295, 1068781), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
