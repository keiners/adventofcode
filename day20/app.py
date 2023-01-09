def run(part_2=False):
    decryption = 811589153 if part_2 else 1
    runs = 10 if part_2 else 1
    
    fileName = "day20/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    lines = [int(i) * decryption for i in lines]
    
    indices = list(range(len(lines)))
    
    for i in list(range(len(lines))) * runs:
        number_to_move = lines[i]
        if number_to_move==0: continue
        
        indices.pop(old_index := indices.index(i))
        indices.insert((old_index + number_to_move) % len(indices), i)
            
    zero_index = indices.index(lines.index(0))
    result_indices = [ (zero_index + i) % len(lines) for i in [1000, 2000, 3000]]
    print(sum([lines[indices[i]] for i in result_indices]))

run()
run(True)
