def run():
    
    fileName = "day21/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    input = {}
    for line in lines:
        split_ = line.split(":")
        a = split_[0]
        b = split_[1].strip()
        if b.isdigit():
            b = int(b)
        else:
            b = b.split(" ")
        input[a] = b

    def find_value(key):
        value = input[key]
        if isinstance(value, int):
            return value
        else: 
            x = find_value(value[0]) 
            y = find_value(value[2])
            if key=="root":
                return eval(f"{x} {value[1]} {y}")
            return eval(f"{x} {value[1]} {y}")

    answer_1 = find_value("root")
    print("PART 1:")
    print(f"Answer: {int(answer_1)}")
    
    
    print("PART 2:")
    def find_value_humn(key, calcs = []):
        value = input[key]
        if value == None:
            return None, calcs
        elif isinstance(value, int):
            return value, calcs
        else: 
            x, calcs = find_value_humn(value[0], calcs) 
            y, calcs = find_value_humn(value[2], calcs)
            if key=="root":
                calcs.append([x, value[1], y])
                return calcs
            if x is None or y is None:
                calcs.append([x, value[1], y])
                return None, calcs
            return eval(f"{x} {value[1]} {y}"), calcs
    

    input["humn"] = None
    foo = find_value_humn("root")
    
    humn = 0
    for i in reversed(foo):
        a = i[2] if i[0] is None else i[0]
        if i[1] == '+':
            humn = humn - a
        elif i[1] == '-':
            humn = humn + a
        elif i[1] == '*':
            humn = humn / a
        elif i[1] == '/':
            humn = humn * a
    
    print(f"Answer: {int(humn)}")

run()
