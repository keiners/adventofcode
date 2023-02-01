def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day18/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = sum_solutions(lines, ordered=False)
    a2 = sum_solutions(lines, ordered=True)
    return (a1, a2)

def sum_solutions(lines, ordered):
    solutions = []
    for line in lines:
        solutions.append(solve_line(line, ordered))
    return sum(solutions)

def solve_line(line, ordered):
    while "(" in line:
        substring = get_in_parentheses(line)
        solved_substring = solve(substring, ordered)
        line = line.replace(f"({substring})", solved_substring, 1)
    return int(solve(line, ordered))

def get_in_parentheses(line):
    for i,a in enumerate(line):
        if a == "(":
            start = i
        elif a == ")":
            return get_in_parentheses(line[start+1:i])
    return line

def solve(line, ordered=False):
    args = line.split(" ")
    if len(args) == 3:
        solution = str(eval(line))
        return solution
    else:
        i = args.index("+") if ordered and "+" in line else 1
        subline = f"{args[i-1]} {args[i]} {args[i+1]}"
        solved_subline = str(eval(subline))
        new_line = line.replace(subline, solved_subline, 1)
        return solve(new_line, ordered)


a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
