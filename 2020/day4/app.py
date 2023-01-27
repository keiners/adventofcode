import re
def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day4/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1 = part1(lines)
    a2 = part2(lines)
    return (a1, a2)

def part1(lines):
    req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    fields = {0: set()}
    passport_n = 0
    for line in lines:
        if line == "":
            passport_n += 1
            fields[passport_n] = set()
            continue
        for pair in line.split(" "):
            fields[passport_n].add(pair.split(":")[0])
    valid_passports = 0
    for v in fields.values():
        if any(field not in v for field in req_fields): continue
        else: valid_passports += 1
    return valid_passports

def part2(lines):
    req_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    fields = {0: {}}
    passport_n = 0
    for line in lines:
        if line == "":
            passport_n += 1
            fields[passport_n] = {}
            continue
        for pair in line.split(" "):
            k,v = pair.split(":")
            fields[passport_n][k] = v

    valid_passports = 0
    for field in fields.values():
        if any(req not in field for req in req_fields):
            continue
        else:
            byr = int(field["byr"])
            iyr = int(field["iyr"])
            eyr = int(field["eyr"])
            if not (1920 <= byr <= 2002 and 2010 <= iyr <= 2020 and 2020 <= eyr <= 2030):
                continue
            
            hgt = field["hgt"]
            if hgt[-2:] == "cm":
                height = re.findall("\d+", hgt)[0]
                if not (150 <= int(height) <= 193):
                    continue
            elif hgt[-2:] == "in":
                height = re.findall("\d+", hgt)[0]
                if not (59 <= int(height) <= 76):
                    continue
            else: continue
            
            hcl = field["hcl"]
            if hcl[0] != "#": continue
            else:
                valid_hcl = True
                for char in hcl[1:]:
                    if char not in "0123456789abcdef":
                        valid_hcl = False
                        break
                if not valid_hcl: continue
                
            ecl = field["ecl"]
            if ecl not in ["amb","blu","brn","gry","grn","hzl","oth"]: continue
            
            pid = field["pid"]
            if len(pid) != 9 or not pid.isdigit(): continue

            valid_passports += 1
    return valid_passports


a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
