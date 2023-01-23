import re, math, itertools
import numpy as np
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2021/day19/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    print((a1,a2))
    return (a1, a2)

def part1(lines):
    print("RUN PART 1")
    scanners = {}
    scanner_count = 0
    for line in lines:
        if line[:3] == "---":
            scanner = int(re.findall("\d+",line)[0])
            scanners[scanner] = []
        elif line != "":
            scanner_count += 1
            #print(line)
            x,y,z = (int(i) for i in re.findall("-?\d+",line))
            #print((x,y,z))
            scanners[scanner].append((x,y,z))
    foo1 = scanner_count
    foo2 = 12*(len(scanners)-1)
    print(f"answer: {foo1-foo2}")
        
    beacons = {k:set() for k in scanners}
    for k,v in scanners.items():
        for b in v:
            beacons[k].add(b)
    while True:
        stop_run = True
        for b in beacons:
            if b==0:continue
            elif len(beacons[b]) > 0:
                stop_run = False
                break
        #for k,v in beacons.items():
            #print(f"L {k}: {len(v)}")
        if stop_run:
            break
        new_beacons = {k:set() for k in beacons}
        for scanner1 in [k for k in beacons.keys()]:
            for scanner2 in [k for k in beacons.keys()]:
                if scanner1 >= scanner2: continue
                matched_one = False
                matched_two = False
                matches = []
                #print(f"Compare {scanner1}-{scanner2}")
                for beacon1 in [b for b in beacons[scanner1]]:
                    if matched_two: break
                    for beacon2 in [b for b in beacons[scanner2]]:
                        map1 = [distance_3d(beacon1, (x,y,z)) for x,y,z in beacons[scanner1]]
                        map2 = [distance_3d(beacon2, (x,y,z)) for x,y,z in beacons[scanner2]]
                        common = common_member(map1, map2)
                        if len(common) > 10:
                            if not matched_one:
                                matches = []
                                matches.append(beacon1)
                                matches.append(beacon2)
                                matched_one = True
                                continue
                            else:
                                matches.append(beacon1)
                                matches.append(beacon2)
                                matched_two = True
                                #print(f"SAME BEACONS: {matches[0]} == {matches[1]}")
                                #print(f"SAME BEACONS: {matches[2]} == {matches[3]}")
                                permutations = list(itertools.permutations([0,1,2]))
                                for perm in permutations:
                                    px,py,pz = perm
                                    if abs(matches[0][0] - matches[2][0]) == abs(matches[1][px] - matches[3][px]):
                                        if abs(matches[0][1] - matches[2][1]) == abs(matches[1][py] - matches[3][py]):
                                            assert abs(matches[0][2] - matches[2][2]) == abs(matches[1][pz] - matches[3][pz])
                                            break
                                dx,dy,dz = -1,-1,-1
                                if (matches[0][0] < matches[2][0]) == (matches[1][px] < matches[3][px]):
                                    dx = 1
                                if (matches[0][1] < matches[2][1]) == (matches[1][py] < matches[3][py]):
                                    dy = 1
                                if (matches[0][2] < matches[2][2]) == (matches[1][pz] < matches[3][pz]):
                                    dz = 1
                                scanner_x = matches[0][0] - dx * matches[1][px]
                                scanner_y = matches[0][1] - dy * matches[1][py]
                                scanner_z = matches[0][2] - dz * matches[1][pz]
                                
                                for beacon in beacons[scanner1]:
                                    new_beacons[scanner1].add(beacon)
                                for beacon in beacons[scanner2]:
                                    x0,y0,z0 = (beacon[px],beacon[py],beacon[pz])
                                    x1 = dx * x0 + scanner_x
                                    y1 = dy * y0 + scanner_y
                                    z1 = dz * z0 + scanner_z
                                    new_beacons[scanner1].add((x1,y1,z1))
        beacons = new_beacons
    return len(beacons[0])


def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return (a_set & b_set)
    else:
        return []

def part2(lines):
    return 0

a=[1,2,3,4]
b=[3,4,5,6]
#print(common_member(a,b))

assert run(True) == (79, 0), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
