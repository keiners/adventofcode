import queue

def run(queueLength):
    f = open("day6/input.txt", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    for line in lines:
        return str(getStartIndex(line, queueLength))

def getStartIndex(line, queueLength):
    q = queue.Queue(queueLength)
    index = 0
    for c in line:
        if q.full():
            if startOfPacket(q):
                break
            else:
                q.get()
        q.put(c)
        index += 1
    return index
        
def startOfPacket(q):
    qList = list(q.queue)
    qList.sort()
    for i in range(len(qList) - 1):
        if qList[i] == qList[i+1]:
            return False
    return True

assert getStartIndex("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
assert getStartIndex("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19

print("Answer part 1: "+run(4))
print("Answer part 2: "+run(14))