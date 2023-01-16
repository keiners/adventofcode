def run():
    f = open("day2/input.txt", "r")
    lines = f.readlines()
    score = 0
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
        my_hand = getHandFromResult(line[0], line[2])
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
    
def getHandFromResult(op_hand, result):
    myHand = ""
    if result == "Y":
        myHand = op_hand
    elif result == "X":
        if op_hand == "A":
            myHand = "C"
        elif op_hand == "B":
            myHand = "A"
        else:
            myHand = "B"
    elif result == "Z":
        if op_hand == "A":
            myHand = "B"
        elif op_hand == "B":
            myHand = "C"
        else:
            myHand = "A"
    return getHand(myHand)
 
run()
run2()