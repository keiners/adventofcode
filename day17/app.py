def run():
    fileName = "day17/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    assert len(lines) == 1
    jet = list(lines[0])
    
    board = [["." for i in range(7)] for i in range(3)]
    shapes = ["..####.", "...#.....###.....#...", "....#......#....###..", "..#......#......#......#....", "..##.....##..."]
    shape_heights = [1,3,3,4,2]
    
    for i in range(6):
        board = add_rows(board, shape_heights[i % 5])
        board = add_shape(board, shapes[i % 5])
            
def add_rows(board, rows):
    board.reverse()
    for i in range(rows):
        board.append(["." for i in range(7)])
    board.reverse()
    #print_board(board)
    return board

def add_shape(board, shape):
    shapes = ["@", "#"]
    board[0][2] = shapes[shape]
    i=0
    while True:
        i += 1
        if i<len(board) and board[i][2] == ".":
            board[i-1][2] = "."
            board[i][2] = shapes[shape]
        else: break
    #print_board(board)
    return board

def print_board(board):
    print("BOARD:")
    for row in board:
        print(row)

run()