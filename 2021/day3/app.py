def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day3/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    bit_sums = [sum([int(line[i]) for line in lines]) for i in range(len(lines[0]))]
    gamma = "".join(["1" if i > len(lines) / 2 else "0" for i in bit_sums])
    epsilon = "".join(["1" if i == "0" else "0" for i in gamma])
    return  int(gamma, 2) * int(epsilon, 2)

def part2(lines):
    oxy_bits = list(lines)
    co2_bits = list(lines)
    index = 0
    while len(oxy_bits) != 1 or len(co2_bits) != 1:
        if len(oxy_bits) != 1:
            oxy_sum = sum([int(line[index]) for line in oxy_bits])
            if oxy_sum >= len(oxy_bits)/2:
                oxy_bits = [line for line in oxy_bits if line[index] == "1"]
            else:
                oxy_bits = [line for line in oxy_bits if line[index] == "0"]
        if len(co2_bits) != 1:
            co2_sum = sum([int(line[index]) for line in co2_bits])
            if co2_sum >= len(co2_bits)/2:
                co2_bits = [line for line in co2_bits if line[index] == "0"]
            else:
                co2_bits = [line for line in co2_bits if line[index] == "1"]
        index +=1
    return int(oxy_bits[0], 2) * int(co2_bits[0], 2)

assert run(True) == (198, 230)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
