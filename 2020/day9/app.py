def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day9/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines, a1)

    return (a1, a2)

def part1(lines):
    numbers = [int(i) for i in lines]
    preamble = 25
    for i,n in enumerate(numbers[preamble:]):
        valid_n = False
        for j,n2 in enumerate(numbers[0+i:preamble+i]):
            for n3 in numbers[0+i+j+1:preamble+i]:
                if n2+n3 == n:
                    valid_n = True
                    break
            if valid_n:
                break
        if valid_n:
            valid_n = False
            continue
        else:
            return n

def part2(lines, a1):
    numbers = [int(i) for i in lines]
    start = 0
    added_numbers = 0
    while True:
        added_numbers = [numbers[start], numbers[start+1]]
        for j in numbers[start+2:]:
            sum_added_n = sum(added_numbers)
            if sum_added_n == a1:
                return min(added_numbers) + max(added_numbers)
            elif sum_added_n > a1:
                start += 1
                break
            else:
                added_numbers.append(j)
            

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
