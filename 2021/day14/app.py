def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day14/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
        
    a1 = polymer_insertion(lines, 10)
    a2 = polymer_insertion(lines, 40)

    return (a1, a2)

def pairs_in_polymer(polymer):
    return [polymer[i]+polymer[i+1] for i in range(len(polymer)-1)]

def get_rules(args):
    rules = {}
    for rule in args:
        a,b = rule.split(" -> ")
        rules[a] = b
    return rules

def polymer_insertion(lines, steps):
    polymer = lines[0]
    rules = get_rules(lines[2:])
    
    pairs_count = {}
    for pair in pairs_in_polymer(polymer):
        if pair in pairs_count:
            pairs_count[pair] += 1
        else:
            pairs_count[pair] = 1
    
    for i in range(steps):
        new_pairs_count = {}
        for k,v in pairs_count.items():
            k1,k2 = k
            for new_pair in [k1+rules[k], rules[k]+k2]:
                if new_pair in new_pairs_count:
                    new_pairs_count[new_pair] += v
                else:
                    new_pairs_count[new_pair] = v
        pairs_count = new_pairs_count
    
    letter_count = {polymer[-1]:1}
    for k,v in pairs_count.items():
        c = k[0]
        if c in letter_count:
            letter_count[c] += v
        else:
            letter_count[c] = v
    
    counter = [int(v) for v in letter_count.values()]
    return max(counter) - min(counter)


assert run(True) == (1588, 2188189693529), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
