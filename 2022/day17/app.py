import re

def run(rocks):
    fileName = "day17/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    assert len(lines) == 1
    jet = list(lines[0])
    jet_index = 0
    
    board = []
    shapes = ["..####.", "...#.....###.....#...", "....#......#....###..", "..#......#......#......#....", "..##.....##..."]

    for i in range(rocks):
        board = add_rows(board, 3)
        board = add_shape(board, shapes[i % 5])
        board,jet_index = move_shape(board,jet,jet_index)
        board = remove_empty_lines(board)

    print("Height after "+str(rocks)+" rocks: "+str(len(board)))

def add_rows(board, rows):
    board.reverse()
    for i in range(rows):
        board.append(["." for i in range(7)])
    board.reverse()
    return board

def add_shape(board, shape):
    lines = re.findall('.......', shape)
    board = add_rows(board, len(lines))
    for i in range(len(lines)):
        board[i] = list(lines[i])
    return board

def move_shape(board, jet, jet_index=0):
    shape = []
    for i in range(4):
        for j in range(7):
            if board[i][j] == "#":
                shape.append((i,j))
    while True:
        board, shape = move_jet(board, shape, jet[jet_index])
        jet_index = (jet_index+1) % len(jet)
        if can_move_down(board, shape):
            for i,j in shape:
                board[i][j] = "."
            for i,j in shape:
                board[i+1][j] = "#"
            shape = [(i+1,j) for i,j in shape]
        else: break
    for i,j in shape:
        board[i][j] = "@"
    return board, jet_index

def can_move_down(board, shape):
    for i,j in shape:
        if i==len(board)-1 or board[i+1][j] == "@": 
            return False
    return True

def remove_empty_lines(board):
    for i in range(len(board)):
        for c in board[i]:
            if c != ".":
                empty_lines = i
                break
        else: continue
        break
    board = board[empty_lines:]
    return board

def move_jet(board, shape, jet):
    push = 1 if jet == ">" else -1
    for i,j in shape:
        if not 0<=j+push<=6 or board[i][j+push] == "@":
            return board, shape
    for i,j in shape:
        board[i][j] = "."
    for i,j in shape:
        board[i][j+push] = "#"
    shape = [(i,j+push) for i,j in shape]
    return board,shape

run(2022)