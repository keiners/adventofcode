def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day16/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    line = lines[0]
    bin1 = to_bin(line)
    a1 = decode_bin(bin1)
    a2 = part2(bin1)
    print((a1,a2))
    return (a1, a2)

def to_bin(line):
    binary = ""
    for c in line:
        d = int(c, 16)
        b = format(d,"04b")
        binary += str(b)
    return binary

def decode_bin(binary):
    print(f"Bin: {binary}")
    V = int(binary[:3], 2)
    T = int(binary[3:6], 2)
    if T == 4:
        print("T = 4")
        i = 6
        numbers = []
        while True:
            if binary[i] == "1":
                numbers.append(binary[i+1:i+5])
                i += 5
            else:
                numbers.append(binary[i+1:i+5])
                break
        remaining_bin = binary[i+5:]
        number_string = "".join([n for n in numbers])
        print(int(number_string, 2))
        V += decode_bin(remaining_bin)
    else:
        print("T != 4")
        I = binary[6]
        if I == "0":
            print("I == 0")
            length_b = binary[7:7+15]
            length = int(length_b, 2)
            print(length)
            sub_packets_all = binary[7+15:7+15+length]
            print(len(sub_packets_all))
            V += decode_bin(sub_packets_all)
                
        else:
            print("I != 0")
            length_b = binary[7:7+11]
            length = int(length_b, 2)
            print(length)
            sub_packets = []
            for i in range(length):
                sub_packets.append(binary[7+11+11*i:7+11+11*(i+1)])
            print(sub_packets)
            print([decode_bin(b) for b in sub_packets])
            for b in sub_packets:
                V += decode_bin(b)        
    return V

def part2(line):
    return 0

assert run(True) == (16, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
