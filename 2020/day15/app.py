import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day15/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    numbers = [int(i) for i in lines[0].split(",")]
    a1 = part1(numbers, 2020)
    a2 = part2(numbers, 30000000)

    return (a1, a2)

def part1(numbers, turns):
    last_spoken = {}
    times_spoken = {}
    previous_n = numbers[0]
    
    for i in range(1, turns+1):
        if i <= len(numbers):
            n = numbers[i-1]
            last_spoken[n] = [i]
            times_spoken[n] = 1
            previous_n = n
        elif times_spoken[previous_n] == 1:
            previous_n = 0
            last_spoken[0] = [last_spoken[0][-1], i]
            times_spoken[previous_n] += 1
        else:
            previous_n = last_spoken[previous_n][-1] - last_spoken[previous_n][-2]
            if previous_n in times_spoken:
                times_spoken[previous_n] += 1
                last_spoken[previous_n] = [last_spoken[previous_n][-1], i]
            else:
                times_spoken[previous_n] = 1
                last_spoken[previous_n] = [i]
    return previous_n

def part2(numbers, turns): #FIXME: Works but very slow
    last_spoken = {}
    times_spoken = {}
    num_after = {}
    for i in range(1, turns+1):
        if i <= len(numbers):
            new_n = numbers[i-1]
            last_spoken[new_n] = i
            times_spoken[new_n] = 1
        elif times_spoken[previous_n] == 1:
            new_n = 0
            num_after[0] = i - last_spoken[0]
            last_spoken[0] = i
            times_spoken[0] += 1
        else:
            new_n = num_after[previous_n]
            if new_n in times_spoken:
                times_spoken[new_n] += 1
                num_after[new_n] = i - last_spoken[new_n]
                last_spoken[new_n] = i
            else:
                times_spoken[new_n] = 1
                last_spoken[new_n] = i
        previous_n = new_n
    return previous_n

assert run(True) == (436, 175594), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
