import re

def run():
    fileName = "day15/input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    sensors = []
    beacons = []
    for line in lines:
        x,y,x2,y2 = [int(i) for i in re.findall(r'-?\d+', line)]
        distance = dist(x,y,x2,y2)
        sensor = Sensor(x,y,distance)
        sensors.append(sensor)
        beacons.append((x2,y2))
    
    #simPart1(sensors, beacons)
    simPart2(sensors, beacons)
    #test(sensors, beacons)

def simPart1(sensors, beacons):
    maxDist = max([s.distance for s in sensors])
    minX = min([s.x for s in sensors])
    maxX = max([s.x for s in sensors])
    xRange = (minX - maxDist, maxX + maxDist)
    invalidPositions = 0
    for i in range(xRange[0], xRange[1]+1):
        x,y = (i,2000000)
        if (x,y) in beacons:
            continue
        for sensor in sensors:
            distToSensor = dist(x,y,sensor.x,sensor.y)
            if distToSensor <= sensor.distance:
                invalidPositions += 1
                break
    print("Part 1: "+str(invalidPositions))
    
 
def _simPart2(sensors, beacons): # too slow
    for x in range(0,4000000+1):
        for y in range(0,4000000+1):
            if (x,y) in beacons:
                continue
            else: 
                validPos = True
                for sensor in sensors:
                    distToSensor = dist(x,y,sensor.x,sensor.y)
                    if distToSensor <= sensor.distance:
                        validPos = False
                        break
                if validPos:
                    print((x,y))
                    return (x*4000000+y)
                
def simPart2(sensors, beacons): # too slow
    coordinateSets = []
    for sensor in sensors:
        possibleCoordinates = find_coordinates_by_distance(sensor.x, sensor.y, sensor.distance+1)
        possibleCoordinates = filterCoordinates(possibleCoordinates, 0, 4000000)
        coordinateSets.append(possibleCoordinates)
    common_ints = findCommon(coordinateSets)
    print(common_ints)
    
def findCommon(lists):
    # create an empty set to store the integers that are found in more than one list
    common_ints = set()

    # loop through each list
    for i in range(len(lists)):
        # loop through each integer in the current list
        for j in range(len(lists[i])):
            # check if the current integer is in any of the other lists
            for k in range(i+1, len(lists)):
                if lists[i][j] in lists[k]:
                    # add the integer to the set of common integers
                    common_ints.add(lists[i][j])

    # print the set of common integers
    #print(common_ints)
    return common_ints

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def filterCoordinates(coordinates, min, max):
    return [c for c in coordinates if min <= c[0] <= max and min <= c[1] <= max]

class Sensor:
  def __init__(self, x, y, distance):
    self.x = x
    self.y = y
    self.distance = distance

def find_coordinates_by_distance(x, y, d):
    foo = set()
    for i in range(d+1):
        foo.add((x-i, y-(d-i)))
        foo.add((x-i, y+(d-i)))
        foo.add((x+i, y-(d-i)))
        foo.add((x+i, y+(d-i)))
    return foo
        
run()
# Sensor at x=2, y=18: closest beacon is at x=-2, y=15


