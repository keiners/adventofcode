def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day6/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    a1 = count_fish(lines, 80)
    a2 = count_fish(lines, 256)

    return (a1, a2)

def count_fish(lines, days):
    fish = [int(i) for i in lines[0].split(",")]
    fish = {1:fish.count(1),
            2:fish.count(2),
            3:fish.count(3),
            4:fish.count(4),
            5:fish.count(5),
            6:fish.count(6)}
    
    for _ in range(days):
        fish_next_day = {0:0, 1:0, 2:0, 3:0, 4:0, 5: 0, 6:0, 7:0, 8:0}
        for k,v in fish.items():
            if v == 0:
                continue
            else:
                if k == 0:
                    fish_next_day[6] += v
                    fish_next_day[8] += v
                else:
                    fish_next_day[k-1] = fish_next_day[k-1] + v
        fish = fish_next_day
    sum = 0
    for v in fish.values():
        sum += v
    return sum

assert run(True) == (5934, 26984457539)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")

