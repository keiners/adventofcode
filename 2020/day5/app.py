import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day5/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    return (a1, a2)

def part1(lines):
    
    max_id = 0
    for line in lines:
        a,b = 0,127
        x,y = 0,7
        for c in line:
            if a==b and x!=y:
                if c == "R":
                    x = ((y-x+1)//2) + x
                elif c == "L":
                    y = ((y-x)//2) + x
            elif c == "F":
                b = ((b-a)//2) + a
            elif c == "B":
                a = ((b-a+1)//2) + a
            if a==b and x==y:
                    if (a*8 + x) > max_id:
                        max_id = a*8 + x
                    continue
    return max_id
def part2(lines):
    free_seats = []
    for line in lines:
        a,b = 0,127
        x,y = 0,7
        for c in line:
            if a==b and x!=y:
                if c == "R":
                    x = ((y-x+1)//2) + x
                elif c == "L":
                    y = ((y-x)//2) + x
            elif c == "F":
                b = ((b-a)//2) + a
            elif c == "B":
                a = ((b-a+1)//2) + a
            if a==b and x==y:
                free_seats.append((a,x))
                continue
    sorted_set = sorted(set([(a*8 + x) for a,x in free_seats]))
    for i in sorted_set:
        if i+1 not in sorted_set and i+2 in sorted_set:
            return i+1


a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
