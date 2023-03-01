import re

def run():
    fileName = "2022/day15/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    sensors = {}
    beacons = []
    for line in lines:
        sx,sy,bx,by = [int(i) for i in re.findall(r'-?\d+', line)]
        distance = manhattan_distance(sx,sy,bx,by)
        sensors[sy + sx*1j] = distance
        beacons.append(by + bx*1j)
    
    a1 = part1(sensors, beacons, 2000000)
    print(f"Answer 1: {a1}")
    a2 = part2(sensors, 4000000)
    print(f"Answer s: {a2}")

def part1(sensors, beacons, target_row):
    invalid_ranges = get_invalid_ranges(sensors, target_row)
    answer = int(sum([len(list(r)) for r in reduce_ranges(invalid_ranges)]))
    answer = answer - len([b for b in beacons if int(b.real) == target_row]) # remove beacons on target row
    return answer

def part2(sensors, max_area):
    valid_area = range(0,max_area+1)
    for y in valid_area:
        go_next = False
        ranges = get_invalid_ranges(sensors, y)
        for r in ranges:
            if valid_area.start in r and valid_area.stop-1 in r:
                go_next = True
                break
        if not go_next:
            for r in ranges:
                if r.stop <= valid_area.start:
                    continue
                else:
                    beacon_x = r.stop
                    break
            print(f"Distress beacon at {(beacon_x,y)}")
            return int(beacon_x * 4000000 + y)

def get_invalid_ranges(sensors, target_row):
    invalid_ranges = []
    for sensor,dist in sensors.items():
        if sensor.real - dist <= target_row <= sensor.real + dist: # if sensor reading reaches target row
            invalid_row_radius = dist - abs(target_row - sensor.real)
            start = int(sensor.imag - invalid_row_radius)
            stop = int(sensor.imag + invalid_row_radius)
            invalid_ranges.append(range(start, stop+1))
    return reduce_ranges(invalid_ranges)

def is_in_range(ranges, x):
    for r in ranges:
        if x in r:
            return True
    return False

def reduce_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x.start) # sort ranges by starting value
    merged_ranges = [sorted_ranges[0]] # initialize list of merged ranges with first range
    for r in sorted_ranges[1:]:
        if r.start <= merged_ranges[-1].stop: # if the next range overlaps with the last merged range
            merged_ranges[-1] = range(merged_ranges[-1].start, max(merged_ranges[-1].stop, r.stop)) # merge the two ranges
        else:
            merged_ranges.append(r) # add the next range to the list of merged ranges
    return merged_ranges


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
        
run()
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15


