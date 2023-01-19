import re, math
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day18/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    current_line = lines[0]
    for line in lines[1:]:
        print("########################")
        print(current_line)
        print("+")
        print(line)
        new_line = add(current_line, line)
        #print(new_line)
        new_line2 = explode_and_split(new_line)
        print("=")
        print(new_line2)
        current_line = new_line2
        #break
    print("DONE")
    #print(current_line)
        
        

def part2(lines):
    return 0

def add(left, right):
    return f"[{left},{right}]"

def explode_and_split(input):
    if type(input) == list:
        input = str(input).replace(" ", "")
    nest = 0
    while True:
        nest = 0
        exploded = False
        split = False
        for i,c in enumerate(input):
            matches = re.findall("\d+", input)
            if any(x>100 for x in [int(y) for y in matches]):
                print(input)
                print("EXIT")
                #exit()
            #print(input)
            if nest > 4:
                end_of_pair = i + input[i:].index("]") + 1
                input = explode(input[:i-1],
                                input[i-1:end_of_pair],
                                input[end_of_pair:])
                exploded = True
                break
            elif c == "[":
                nest += 1
            elif c == "]":
                nest += -1
        if not exploded:
            matches = re.findall("\d{2,}", input)
            if matches:
                to_split = matches[0]
                index = input.find(to_split)
                x,y = [int(to_split)//2, math.ceil(int(to_split)/2)]
                input = input[:index] + f"[{x},{y}]" + input[index+2:]
                #print(input)
                if int(x)>100 or int(y)>100:
                    print((x,y))
                    print("EXIT")
                    #exit()
                split = True
        if not exploded and not split:
            return input

def explode(start, pair, end):
    #print("EXPLODE "+start+pair+end)
    #print("PAIR: "+pair)
    x,y = eval(pair)
    matches = re.findall("\d+", start)
    if matches:
        #print("SWAP START")
        swap_with = matches[-1]
        index = start.rfind(swap_with)
        start = start[:index]+str(int(swap_with)+int(x))+start[index+1:]
    matches = re.findall("\d+", end)
    if matches:
        #print("SWAP END")
        swap_with = matches[0]
        len_swap = len(swap_with)
        index = end.find(swap_with)
        
        end = end[:index]+str(int(swap_with)+int(y))+end[index+len_swap:]
        #print(end)
    pair = "0"
    #print(start+pair+end)
    return start+pair+end

def run_tests():
    ins = {"[[[[[9,8],1],2],3],4]": "[[[[0,9],2],3],4]",
            "[7,[6,[5,[4,[3,2]]]]]": "[7,[6,[5,[7,0]]]]",
            "[[6,[5,[4,[3,2]]]],1]": "[[6,[5,[7,0]]],3]",
            "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]": "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"}
    for k,v in ins.items():
        #o = explode_and_split("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        #print(o)
        #break
        assert explode_and_split(k) == v, f"WROONG {k} - {v}"
    exit()
#run_tests()
        
        
def get_magnitude(arg):
    magnitude = 0
    if type(arg) == list:
        arg = str(arg).replace(" ", "")
    output = str(arg)
    while True:
        matches = re.findall("\d+,\d+", output)
        if len(matches) == 0:
            break
        for match in matches:
            x,y = [int(i) for i in match.split(",")]
            output = output.replace(f"[{match}]", str(3*x + 2*y))
    return int(output)

def test_magnitude():
    arg1 = [[9,1],[1,9]]
    arg2 =  "[[9,1],[1,9]]"
    foo1 = get_magnitude(arg1)
    foo2 = get_magnitude(arg2)
    assert foo1 == 129 and foo2 == 129, "failed magnitude test"
#test_magnitude()

assert run(True) == (4140, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
