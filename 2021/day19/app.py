import re, math
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
    
    #print(beacon_map)
    #print(scanners[0])
    #print(beacons_from_base)
    #all_beacons = [(x,y,z) for x,y,z in scanners[0]]
    length_map = []
    sc = {k:set() for k in scanners}
    common_beacons = 0
    #unique_scanners = {k:v for k,v in scanners.items()}
    for scanner1 in scanners:
        for scanner2 in scanners:
            if scanner1 >= scanner2: continue
            #print(f"Compare {scanner1}-{scanner2}")
            found_common_beacons = False
            for i,beacon1 in enumerate(scanners[scanner1]):
                #if found_common_beacons:
                    #break
                for j,beacon2 in enumerate(scanners[scanner2]):
                    map1 = [distance_3d(beacon1, (x,y,z)) for x,y,z in scanners[scanner1]]
                    map2 = [distance_3d(beacon2, (x,y,z)) for x,y,z in scanners[scanner2]]
                    common = common_member(map1, map2)
                    if len(common) > 10:
                        #print(len(common))
                        #print(f"SAME BEACONS: {beacon1} == {beacon2}")
                        #common_beacons += len(common)
                        found_common_beacons = True
                        
                        
                        common_beacons += 1
                        #sc[scanner1].add(beacon1)
                        sc[scanner2].add(beacon2)
                        
                        break
                        length_check = False
                        for c in common:
                            if not length_check and c != (0):
                                length_check = c
                                break
                        for b in scanners[scanner1]:
                            if distance_3d(b, beacon1) == length_check:
                                beacon3 = b
                                break
                        for b in scanners[scanner2]:
                            if distance_3d(b, beacon2) == length_check:
                                beacon4 = b
                                break
                        #print(f"SAME BEACON2: {beacon3} {beacon4}")
                        
                        x1,y1,z1 = beacon1
                        x2,y2,z2 = beacon2
                        x3,y3,z3 = beacon3
                        x4,y4,z4 = beacon4
                        dx = 1 if x3-x1 > x4-x2 else -1
                        dy = 1 if y3-y1 > y4-y2 else -1
                        dz = 1 if z3-z1 > z4-z2 else -1
                        #print((dx,dy,dz))
                        scanner_conv[str(scanner1)+str(scanner2)] = (dx,dy,dz)
                        
                        scanner_spot = (x1+dx*x2,y1+dy*y2,z1+dz*z2)
                        #print(scanner_spot)
                        combined_map = []
                        m1 = [x-x1,y-y2]
                        for m in map1:
                            length_map.append(m)
                        for m in map2:
                            length_map.append(m)
                        #print(len(common))
                        unique_beacons = len(map1)+len(map2)-(2 * len(common))
                        #print(f"Uniq: {unique_beacons}")
                        common_beacons += len(common)
                        found_common_beacons = True
                        break
    #print(len(set(length_map)))
    foo = 0
    for k,v in sc.items():
        print(f"k: {len(v)}")
        bar = len(scanners[k])-len(sc[k])
        foo += bar
    #print("test:")
    print(foo)
    #print(len(set(sc[0])))
    print(sum([len(v) for v in scanners.values()]) - common_beacons)
    return sum([len(v) for v in scanners.values()]) - common_beacons
    

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
