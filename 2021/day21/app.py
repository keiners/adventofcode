def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day21/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    start1 = int(lines[0][-2:].strip())
    start2 = int(lines[1][-2:].strip())
    
    a1 = part1(start1, start2)
    a2 = part2(start1, start2)

    return (a1, a2)

def part1(start1, start2):
    next_roll = 1
    p1, p2 = start1, start2
    s1, s2 = 0, 0
    rolls = 0
    while True:
        rolls += 3
        p1 = 1 + (p1 + dice_sum(next_roll) - 1) % 10
        s1 += p1
        next_roll = 1 + (next_roll + 2) % 100
        if s1 >= 1000:
            return s2 * rolls
        rolls += 3
        p2 = 1 + (p2 + dice_sum(next_roll) - 1) % 10
        s2 += p2
        next_roll = 1 + (next_roll + 2) % 100
        if s2 >= 1000:
            return s1 * rolls

def dice_sum(first_roll):
    roll = [100] + list(range(1,100))
    return roll[first_roll % 100] + roll[(first_roll + 1) % 100] + roll[(first_roll + 2) % 100]

def part2(start1, start2):
    w1,w2 = roll_quantum(start1,start2,0,0,1)
    print((w1,w2))
    return max((w1,w2))

def roll_quantum(p1,p2,s1,s2,player_to_play):
    return 0,0 # TODO: Too slow, never finishes
    dice_rolls = [a+b+c for a in range(1,4) for b in range(1,4) for c in range(1,4)]
    wins1,wins2 = 0,0
    for d in dice_rolls:
        new_p1,new_p2 = p1,p2
        new_s1,new_s2 = s1,s2
        if player_to_play == 1:
            new_p1 = 1+ (new_p1 + d -1) % 10
            new_s1 += new_p1
        else:
            new_p2 = 1+ (new_p2 + d -1) % 10
            new_s2 += new_p2
        if new_s1 >= 21:
            wins1 += 1
        elif new_s2 >= 21:
            wins2 += 1
        else:
            new_wins1,new_wins2 = roll_quantum(new_p1,new_p2,new_s1,new_s2,1+player_to_play%2)
            wins1 += new_wins1
            wins2 += new_wins2
    return (wins1,wins2)

assert run(True) == (739785, 444356092776315), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
