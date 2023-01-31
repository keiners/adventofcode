def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day11/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    seats = {}
    for y,row in enumerate(lines):
        for x,seat in enumerate(row):
            seats[y+1j*x] = seat
    while True:
        occupy_seats = []
        free_seats = []
        for seat,status in seats.items():
            if status == ".": continue
            adj_occ = occupied_adjacent(seats, seat)
            if status == "L" and adj_occ == 0:
                occupy_seats.append(seat)
            elif status == "#" and adj_occ >= 4:
                free_seats.append(seat)
        if len(occupy_seats) == 0 and len(free_seats)==0:
            return get_occupied_seats(seats)
        for seat in occupy_seats:
            seats[seat] = "#"
        for seat in free_seats:
            seats[seat] = "L"

def occupied_adjacent(seats, position):
    surrounding_seats = [seats[position + y + x * 1j] for x in [-1, 0, 1] for y in [-1, 0, 1] if not (x==0 and y==0) and (position + y + x * 1j) in seats]
    return surrounding_seats.count("#")

def get_occupied_seats(seats):
    return list(seats.values()).count("#")

def part2(lines): #FIXME: Slowish
    seats = {}
    for y,row in enumerate(lines):
        for x,seat in enumerate(row):
            seats[y+1j*x] = seat
    while True:
        occupy_seats = []
        free_seats = []
        for seat,status in seats.items():
            if status == ".": continue
            adj_occ = occupied_in_sight(seats, seat)
            if status == "L":
                if adj_occ == 0:
                    occupy_seats.append(seat)
            elif status == "#":
                if adj_occ >= 5:
                    free_seats.append(seat)
        if len(occupy_seats) == 0 and len(free_seats)==0:
            return get_occupied_seats(seats)
        for seat in occupy_seats:
            seats[seat] = "#"
        for seat in free_seats:
            seats[seat] = "L"

def occupied_in_sight(seats, position):
    count = 0
    for y in [-1,0,1]:
        for x in [-1j, 0, 1j]:
            if y==0 and x==0:
                continue
            multiplier = 1
            while position + (x+y)*multiplier in seats:
                if seats[position + (x+y)*multiplier] == "#":
                    count += 1
                    break
                elif seats[position + (x+y)*multiplier] == "L":
                    break
                else:
                    multiplier += 1
    return count
                

assert run(True) == (37, 26), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
