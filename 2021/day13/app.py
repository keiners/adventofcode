def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day13/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    a1 = part1(lines, 1)
    a2 = part2(lines)

    return (a1, a2)
    
def part1(lines, folds_to_do):
    paper = create_map(lines)
    folds = reversed(read_fold(lines))
    fold_n = 0
    for d,i in folds:
        fold_n += 1
        folded_paper = {}
        if d == "x":
            for k in paper.keys():
                if k.real > i:
                    k2 = complex((i - (k.real - i)), k.imag)
                    folded_paper[k2] = True
                else:
                    folded_paper[k] = True
        else:
            pass
            for k in paper.keys():
                if k.imag > i:
                    k2 = complex(k.real, (i - (k.imag - i)))
                    folded_paper[k2] = True
                else:
                    folded_paper[k] = True
        paper = folded_paper
        if fold_n == folds_to_do:
            return len(paper)
    return paper

def create_map(lines):
    map_ = {}
    for line in lines:
        if line == "":
            break
        x,y = line.split(",")
        map_[int(x) + 1j*int(y)] = True
    return map_

def read_fold(lines):
    folds = []
    for line in reversed(lines):
        if line == "":
            break
        d,i = line.split(" ")[-1].split("=")
        folds.append((d,int(i)))
    return folds

def part2(lines):
    paper = part1(lines, 0)
    x1 = int(min([p.real for p in paper]))
    x2 = int(max([p.real for p in paper]))
    y1 = int(min([p.imag for p in paper]))
    y2 = int(max([p.imag for p in paper]))
    
    print(f"Part 2 answer:")
    for y in range(y1,y2+1):
        row = ""
        for x in range(x1,x2+1):
            if complex(x,y) in paper.keys():
                row += "#"
            else:
                row += " "
        print(row)
    return 0

assert run(True) == (17, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")