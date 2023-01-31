import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day16/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def part1(lines):
    reached_your_ticket, reached_near_tickets = False, False
    ranges = []
    invalid_numbers = []
    for line in lines:
        if line == "your ticket:":
            reached_your_ticket = True
            ranges = reduce_ranges(ranges)
            continue
        elif line == "nearby tickets:":
            reached_near_tickets = True
        elif not reached_your_ticket:
            numbers = [int(i) for i in re.findall("\d+", line)]
            if numbers:
                n0,n1,n2,n3 = numbers
                ranges.append([n0,n1])
                ranges.append([n2,n3])
        elif reached_near_tickets:
            numbers = [int(i) for i in re.findall("\d+", line)]
            for n in numbers:
                valid_n = False
                for r in ranges:
                    if n < r[0]: break
                    elif r[0]<=n<=r[1]:
                        valid_n = True
                        break
                if not valid_n:
                    invalid_numbers.append(n)
    return sum(invalid_numbers)

def reduce_ranges(ranges):
    temp_ranges = [r.copy() for r in ranges]
    temp_ranges.sort(key=lambda x: x[0])
    merged = [temp_ranges[0]]
    for current in temp_ranges:
        previous = merged[-1]
        if current[0] <= previous[1]+1:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged
    
def part2(lines):
    reached_your_ticket, reached_near_tickets = False, False
    ranges = []
    valid_tickets = []
    departure_fields = []
    field_counter = 0
    
    # Parse Input
    for line in lines:
        if line == "your ticket:":
            reached_your_ticket = True
            reduced_ranges = reduce_ranges(ranges)
        elif line == "nearby tickets:":
            reached_near_tickets = True
        elif not reached_your_ticket:
            numbers = [int(i) for i in re.findall("\d+", line)]
            if numbers:
                if line.startswith("departure"):
                    departure_fields.append(field_counter)
                n0,n1,n2,n3 = numbers
                ranges.append([n0,n1])
                ranges.append([n2,n3])
            field_counter += 1
        elif reached_near_tickets:
            invalid_ticket = False
            numbers = [int(i) for i in re.findall("\d+", line)]
            for n in numbers:
                valid_n = False
                for r in reduced_ranges:
                    if n < r[0]: break
                    elif r[0]<=n<=r[1]:
                        valid_n = True
                        break
                if not valid_n:
                    invalid_ticket = True
                    break
            if not invalid_ticket:
                valid_tickets.append(numbers)
        else: 
            numbers = [int(i) for i in re.findall("\d+", line)]
            if numbers:
                my_ticket = numbers
    
    # Map which ticket value position are valid for which field
    ranges = [[ranges[i][0], ranges[i][1], ranges[i+1][0], ranges[i+1][1]] for i in range(0, len(ranges), 2)]
    fields = {}
    for i in range(len(valid_tickets[0])):
        field_set = set(range(len(valid_tickets[0])))
        for ticket in valid_tickets:
            if len(field_set) == 1:
                break
            field_set_for_n = set()
            n = ticket[i]
            for j,r in enumerate(ranges):
                if r[0]<=n<=r[1] or r[2]<=n<=r[3]:
                    field_set_for_n.add(j)
            field_set = field_set.intersection(field_set_for_n)
        fields[i] = field_set
    field_mapping = {}
    
    # Reduce each value position to a single field
    while True:
        solved_fields = set()
        for k,v in fields.items():
            if len(v) == 1:
                f = list(v)[0]
                solved_fields.add(f)
                field_mapping[f] = k
        if len(solved_fields) == 0: break
        for k in fields:
            fields[k] = fields[k] - solved_fields
    
    answer = 1
    for i in departure_fields:
        ticket_index = field_mapping[i]
        answer = answer * my_ticket[ticket_index]
    return answer


a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
