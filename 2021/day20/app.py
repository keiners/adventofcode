def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day20/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    algorithm = lines[0]
    image = {}
    for y,row in enumerate(lines[2:]):
        for x,pixel in enumerate(row):
            image[y + (1j * x)] = get_bit(pixel)
    answer = enhance_image(algorithm, image, rounds=2)
    return answer

def part2(lines):
    algorithm = lines[0]
    image = {}
    for y,row in enumerate(lines[2:]):
        for x,pixel in enumerate(row):
            image[y + (1j * x)] = get_bit(pixel)
    answer = enhance_image(algorithm, image, rounds=50)
    return answer

def enhance_image(algorithm, image, rounds):
    outside_bit = "0"
    for _ in range(rounds):
        new_image = {}
        min_x = int(min([k.imag for k in image]))
        max_x = int(max([k.imag for k in image]))
        min_y = int(min([k.real for k in image]))
        max_y = int(max([k.real for k in image]))
        for y in range(min_y-1,max_y+2):
            for x in range(min_x-1,max_x+2):
                position = y + 1j * x
                binary = get_binary(image, position, outside_bit)
                insert_pixel = algorithm[int(binary, 2)]
                new_image[position] = get_bit(insert_pixel)
        
        if outside_bit == "0":
            outside_bit = get_bit(algorithm[0])
        else:
            outside_bit = get_bit(algorithm[-1])
        image = new_image
        
    if outside_bit == "1": raise Exception("Infinite Lit Bits")
    
    lit_bits = get_lit_bits(image)
    return lit_bits

def get_binary(image, position, outside_bit):
    binary = ""
    for i in [-1-1j, -1, -1+1j, -1j, 0, 1j, 1-1j, 1, 1+1j]:
        if (position + i) not in image:
            binary += outside_bit
        else:
            binary += image[position + i]
    return binary

def get_bit(pixel):
    if pixel == ".":
        return "0"
    elif pixel == "#":
        return "1"
    else:
        raise Exception

def get_lit_bits(image):
    return len([i for i in image.values() if i == "1"])


assert run(True) == (35, 3351), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
