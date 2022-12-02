def run():
    f = open("day2/input.txt", "r")
    lines = f.readlines()
    score = 0
    scoreAlwaysScissor = 0
    for line in lines:
        op_hand = getHand(line[0])
        my_hand = getHand(line[2])
        score += getResult(op_hand, my_hand) + my_hand
    print("Final score part 1: "+str(score))

def run2():
    f = open("day2/input.txt", "r")
    lines = f.readlines()
    score = 0
    for line in lines:
        op_hand = getHand(line[0])
        my_hand = getHand(getMyHand(line[0], line[2]))
        score += getResult(op_hand, my_hand) + my_hand
    print("Final score part 2: "+str(score))

def getResult(opponent, me):
    if opponent==me:
        return 3
    elif opponent == 1:
        if me == 2:
            return 6
        else:
            return 0
    elif opponent == 2:
        if me == 3:
             return 6
        else:
             return 0
    elif opponent == 3:
        if me == 1:
            return 6
        else:
            return 0
    
def getHand(input):
    if input == "A" or input == "X":
        return 1
    elif input == "B" or input == "Y":
        return 2
    elif input == "C" or input == "Z":
        return 3
    
def getMyHand(op_hand, result):
    if result == "Y":
        return op_hand
    elif result == "X":
        if op_hand == "A":
            return "C"
        elif op_hand == "B":
            return "A"
        else:
            return "B"
    elif result == "Z":
        if op_hand == "A":
            return "B"
        elif op_hand == "B":
            return "C"
        else:
            return "A"
 
run()
run2()