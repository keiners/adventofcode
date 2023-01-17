def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day8/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]

    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    digits = [d.split(" ") for d in [line.split(" | ")[1] for line in lines]]
    signals_by_length = {k:0 for k in range(8)}
    for d in [d for sublist in digits for d in sublist]:
        signals_by_length[len(d)] += 1
    return signals_by_length[2] + signals_by_length[4] + signals_by_length[3] + signals_by_length[7]

def part2(lines):
    sum = 0
    for line in lines:
        digit_by_signal = decode_signals(line)
        digits = [''.join(sorted(d)) for d in line.split(" | ")[1].split(" ")]
        sum += int("".join([d for d in [str(digit_by_signal[d]) for d in digits]]))
    return sum

def decode_signals(line):
    digit_to_signal_dict = {}
    
    digits = line.replace(" | "," ").split(" ")
    digits = set(["".join(sorted(d)) for d in digits])
    assert len(digits) == 10, 'digit signal missing from input'
    # map 1, 4, 7, 8
    for d in list(digits):
        if len(d) == 2:
            digit_to_signal_dict[1] = d
        elif len(d) == 4:
            digit_to_signal_dict[4] = d
        elif len(d) == 3:
            digit_to_signal_dict[7] = d
        elif len(d) == 7:
            digit_to_signal_dict[8] = d
        else:
            continue
        digits.remove(d)
    # map 0, 6, 9
    for d in [d for d in digits if len(d)==6]:
        four = list(digit_to_signal_dict[4])
        one = list(digit_to_signal_dict[1])
        if all([i in d for i in four]):
            digit_to_signal_dict[9] = d
            digits.remove(d)
        elif all([i in d for i in one]):
            digit_to_signal_dict[0] = d
            digits.remove(d)
        else:
            digit_to_signal_dict[6] = d
            digits.remove(d)
    # map 2, 3, 5
    for d in [d for d in digits if len(d)==5]:
        one = list(digit_to_signal_dict[1])
        if all([i in d for i in one]):
            digit_to_signal_dict[3] = d
            digits.remove(d)
        else:
            five_or_two = list(d)
            if all([i in digit_to_signal_dict[9] for i in five_or_two]):
                digit_to_signal_dict[5] = d
                digits.remove(d)
            else:
                digit_to_signal_dict[2] = d
                digits.remove(d)

    assert len(digit_to_signal_dict) == 10, 'unable to decode all digits'
    return {v: k for k, v in digit_to_signal_dict.items()}
        
assert run(True) == (26, 61229), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
