def run():
    f = open("day7/input.txt", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    rootDir = Directory("/", None)
    dirIndex = 0
    dirPath = [rootDir]
    for line in lines:
        args = line.split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] == "/":
                    dirPath = dirPath[:1]
                elif args[2] == "..":
                    dirPath = dirPath[:-1]
                else:
                    subDir = last(dirPath).getSubDir(args[2])
                    assert subDir != None
                    dirPath.append(subDir)
            elif args[1] == "ls":
                pass
        elif args[0] == "dir":
            last(dirPath).addSubDir(args[1])
        else:
            last(dirPath).addFile(args[1], args[0])

    rootSize,dirSizes = rootDir.getSize([])
    validDirSizes = [x for x in dirSizes if x < 100000]
    answerPart1 = sum(validDirSizes)
    
    spaceNeeded = 30000000 - (70000000 - rootSize)
    answerPart2 = next(x for x in sorted(dirSizes) if x > spaceNeeded)

    print("Part 1 answer: " + str(answerPart1))
    print("Part 2 answer: " + str(answerPart2))
    assert answerPart1 == 1348005
    assert answerPart2 == 12785886

def last(liste):
    return liste[len(liste)-1]

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.dirs = []
    def getSubDir(self, dirName):
        for d in self.dirs:
            if d.name == dirName:
                return d
        return None
    def addSubDir(self, dirName):
        self.dirs.append(Directory(dirName, self))
    def addFile(self, fileName, fileSize):
        self.files[fileName] = fileSize
    def getSize(self, listOfSizes):
        sizeOfDir = 0
        for i in self.files.values():
            sizeOfDir += int(i)
        for d in self.dirs:
            sizeOfSubDir = d.getSize(listOfSizes)
            sizeOfDir += sizeOfSubDir[0]
            listOfSizes = sizeOfSubDir[1]
        listOfSizes.append(sizeOfDir)
        return [sizeOfDir, listOfSizes]
run()
