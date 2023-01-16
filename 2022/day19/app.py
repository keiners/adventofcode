import re, math
def run(test=False):
    fileName = "day19/input.txt" if not test else "day19/test_input.txt"
    f = open(fileName, "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    blueprints = []
    for line in lines:
        numbers = [int(i) for i in re.findall(r'\d+', line)]
        blueprints.append(numbers)

    run_part_1(blueprints)

def run_part_1(blueprints):
    for blueprint in blueprints:
        cost = Cost(blueprint)
        inventory = Geodes()

        robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        for min in range(1,10):
            print(f"MINUTE: {min} - {inventory.print()}")
            # Robot Building
            if robots["clay"] == 0:
                if inventory.can_build(cost.clay_bot):
                    print("Building clay robot")
                    inventory.build(cost.clay_bot)
                    robots["clay"] += 1
            elif robots["obsidian"] == 0:
                if inventory.can_build(cost.obsidian_bot):
                    print("Building obsidian robot")
                    inventory.build(cost.obsidian_bot)
                    robots["obsidian"] += 1
                        
            # Robot Collection
            inventory.ore += robots["ore"]
            inventory.clay += robots["clay"]
            inventory.obsidian += robots["obsidian"]
            inventory.geodes += robots["geode"]


class Cost:
    def __init__(self, input) -> None:
        self.ore_bot = Geodes(ore=input[1])
        self.clay_bot = Geodes(ore=input[2])
        self.obsidian_bot = Geodes(ore=input[3], clay=input[4])
        self.geode_bot = Geodes(ore=input[5], obsidian=input[6])
class Geodes:
    def __init__(self, ore=0, clay=0, obsidian=0, geodes=0) -> None:
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geodes = geodes
    def print(self):
        return [self.ore, self.clay, self.obsidian, self.geodes]
    def can_build(self, geodes):
        return (self.ore >= geodes.ore and self.clay >= geodes.clay and self.obsidian >= geodes.obsidian)
    def build(self, geodes):
        self.ore = self.ore - geodes.ore
        self.clay = self.clay - geodes.clay
        self.obsidian = self.obsidian - geodes.obsidian
    
run()