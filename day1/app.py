def run(numberOfElves=1):
    f = open("day1/input.txt", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    calorieList = [ 0 ]
    for line in lines:
        if line != "":
            calorieList[-1] += int(line)
        else:
            calorieList.append(0)
    calorieList.sort(reverse=True)
    return sum(calorieList[:numberOfElves])


print("Part 1 answer: " + str(run()))
print("Part 2 answer: " + str(run(3)))
