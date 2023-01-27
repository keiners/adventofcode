import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day2/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    valid_passwords = 0
    for line in lines:
        min,max = [int(i) for i in re.findall("\d+", line)]
        char = line.split(":")[0][-1]
        password = line.split(":")[1].strip()
        if min <= password.count(char) <= max:
            valid_passwords += 1
    return valid_passwords

def part2(lines):
    valid_passwords = 0
    for line in lines:
        min,max = [int(i) for i in re.findall("\d+", line)]
        char = line.split(":")[0][-1]
        password = line.split(":")[1].strip()
        if (password[min-1] == char or password[max-1] == char) and password[min-1] != password[max-1]:
            valid_passwords += 1
    return valid_passwords

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
