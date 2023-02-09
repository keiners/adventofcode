def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day22/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)

    return (a1, a2)

def map_decks(lines):
    decks = {}
    for line in lines:
        if line == "": continue
        elif line.startswith("Player"):
            player = int(line[-2])
            decks[int(line[-2])] = []
        else:
            decks[player].append(int(line))
    return decks
    
def part1(lines):
    decks = map_decks(lines)
    while decks[1] != [] and decks[2] != []:
        decks = play_1(decks)
    cards = [card for player_deck in decks.values() for card in player_deck]
    scores = [(i+1)*n for i,n in enumerate(cards[::-1])]
    return sum(scores)

def play_1(decks):
    if decks[1][0] > decks[2][0]:
        decks[1] = decks[1][1:] + [decks[1][0], decks[2][0]]
        decks[2] = decks[2][1:]
    else:
        decks[2] = decks[2][1:] + [decks[2][0], decks[1][0]]
        decks[1] = decks[1][1:]
    return decks

def part2(lines):
    decks = map_decks(lines)
    while decks[1] != [] and decks[2] != []:
        decks = play_2(decks)
    cards = [card for player_deck in decks.values() for card in player_deck]
    scores = [(i+1)*n for i,n in enumerate(cards[::-1])]
    return sum(scores)

def play_2(decks):
    if len(decks[1]) <= decks[1][0] or len(decks[2]) <= decks[2][0]:
        return play_1(decks)
    else:
        # Start subgame
        sub_decks = {1: decks[1][1:1+decks[1][0]], 2: decks[2][1:1+decks[2][0]]}
        played_decks_1 = set()
        played_decks_2 = set()
        while sub_decks[1] != [] and sub_decks[2] != []:
            played_decks_1.add("".join([str(i) for i in sub_decks[1]]))
            played_decks_2.add("".join([str(i) for i in sub_decks[2]]))
            sub_decks = play_2(sub_decks)
            if "".join([str(i) for i in sub_decks[1]]) in played_decks_1 or "".join([str(i) for i in sub_decks[2]]) in played_decks_2:
                # Mark player 1 as winner if repeating decks
                sub_decks[2] = []
        if sub_decks[2] == []:
            decks[1] = decks[1][1:] + [decks[1][0], decks[2][0]]
            decks[2] = decks[2][1:]
        else:
            decks[2] = decks[2][1:] + [decks[2][0], decks[1][0]]
            decks[1] = decks[1][1:]
        return decks


assert run(True) == (306, 291), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
