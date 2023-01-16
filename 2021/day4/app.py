import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day4/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    return (a1, a2)

def part1(lines):
    numbers = [int(n) for n in lines[0].split(',')]
    boards = []
    for line in lines[1:]:
        if line == "":
            board = Board()
            boards.append(board)
        else:
            row = re.findall(r"\d+", line)
            board.rows.append([int(x) for x in row])
    for b in boards:
        b.set_columns()
    
    for n in numbers:
        for b in boards:
            for row in b.rows:
                if n in row:
                    row[row.index(n)] = -1
            for col in b.cols:
                if n in col:
                    col[col.index(n)] = -1
        for b in boards:
            for row in b.rows:
                if sum(row) == 0-len(row):
                    sum_ = b.sum_unmarked()
                    return sum_ * n
            for col in b.cols:
                if sum(col) == 0-len(col):
                    sum_ = b.sum_unmarked()
                    return sum_ * n
    return 0
            
def part2(lines):
    numbers = [int(n) for n in lines[0].split(',')]
    boards = []
    for line in lines[1:]:
        if line == "":
            board = Board()
            boards.append(board)
            rows = []
        else:
            row = re.findall(r"\d+", line)
            board.rows.append([int(x) for x in row])
    for b in boards:
        b.set_columns()

    boards_remaining = len(boards)
    for n in numbers:
        for b in boards:
            if b.complete:
                continue
            for row in b.rows:
                if n in row:
                    row[row.index(n)] = -1
            for col in b.cols:
                if n in col:
                    col[col.index(n)] = -1
        for b in boards:
            if b.complete:
                continue
            for row in b.rows:
                if sum(row) == 0-len(row):
                    b.complete = True
                    sum_ = b.sum_unmarked()
                    if boards_remaining == 1:
                        return sum_ * n
            for col in b.cols:
                if sum(col) == 0-len(col):
                    b.complete = True
                    sum_ = b.sum_unmarked()
                    if boards_remaining == 1:
                        return sum_ * n
            if b.complete:
                boards_remaining -= 1
    return 0

class Board:
    def __init__(self) -> None:
        self.rows = []
        self.cols = []
        self.complete = False
    def set_columns(self):
        for i in range(len(self.rows[0])):
            self.cols.append([self.rows[j][i] for j in range(len(self.rows))])
        return self.cols
    def sum_unmarked(self):
        sum_ = 0
        for row in self.rows:
            sum_ += sum([n for n in row if n >= 0])
        return sum_

assert run(True) == (4512, 1924)

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
