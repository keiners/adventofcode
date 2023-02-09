def run(test=False):
    fileName = "input.txt" if not test else "test_input.txt"
    f = open(f"2020/day21/{fileName}", "r")
    lines = [line.replace("\n", "") for line in f.readlines()]
    
    a1, mapped_allergens = part1(lines)
    a2 = part2(mapped_allergens)

    return (a1, a2)

def part1(lines):
    ingredients_per_allergen = {}
    input_ingredients = []
    for i,line in enumerate(lines):
        ingredients = []
        for ingredient in line.split(" "):
            if ingredient.startswith("("):
                input_ingredients.extend(ingredients)
                allergens = line[line.index("contains")+9:-1]
                allergens = allergens.replace(",", "")
                allergens = allergens.split(" ")
                for allergene in allergens:
                    if allergene not in ingredients_per_allergen:
                        ingredients_per_allergen[allergene] = ingredients
                    else:
                        ingredients_per_allergen[allergene] = list(set(ingredients_per_allergen[allergene]) & set(ingredients))
                break
            else:
                ingredients.append(ingredient)
    
    counter = 0
    ingredients_with_allergen = set(letter for values in ingredients_per_allergen.values() for letter in values)
    for i in set(input_ingredients):
        if i not in ingredients_with_allergen:
            counter += input_ingredients.count(i)
    return counter, ingredients_per_allergen

def part2(mapped_allergens):
    mapped_allergens = reduce_mapping(mapped_allergens)
    mapped_allergens = sorted(mapped_allergens.values(), key=lambda x: [k for k, v in mapped_allergens.items() if v == x][0])
    return ",".join(mapped_allergens,)

def reduce_mapping(mapping):
    reduced_mapping = {}
    letters = set(letter for values in mapping.values() for letter in values)
    while len(letters) > 0:
        for key, values in mapping.items():
            if len(values) == 1 and values[0] in letters:
                letter = values[0]
                reduced_mapping[key] = letter
                letters.remove(letter)
                break
        for key, values in mapping.items():
            mapping[key] = [value for value in values if value != letter]
    return reduced_mapping

assert run(True) == (5, "mxmxvkd,sqjhc,fvjkl"), 'failed test input'

a1,a2 = run()
print(f"Part 1 answer: {a1}")
print(f"Part 2 answer: {a2}")
