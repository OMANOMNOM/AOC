def is_ingredient_fresh(fresh_id_ranges, ingredient_id):
    """Return True if Ingredient_id is fresh

    Args:
        fresh_id_ranges (_type_): _description_
        ingredient_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    for id_range in fresh_id_ranges:
        if ingredient_id >= id_range["start"] and ingredient_id <= id_range["end"]:
            print(f"Fresh ingredient found: id {ingredient_id}")
            return True
    return False


# Read in fresh ingredient ID ranges
is_fresh_ids = True
fresh_id_ranges = list()
available_ingredients = list()
with open(r"C:\Projects\Code\AOC\2025 - python\day-5\problem-1.txt") as input_file:
    for line in input_file:
        if is_fresh_ids:
            if line.strip() == "":
                is_fresh_ids = False
            else:
                substrs = str.split(line.strip(),"-",) 
                fresh_id_ranges.append({"start": int(substrs[0]), "end": int(substrs[1])})
                if (int(substrs[0]) > int(substrs[1])):
                    print("error")
                # process freshIDs 
        else:
            available_ingredients.append(int(line))
            #process available ingredient IDs


total_fresh_ingredients = 0
# Loop through available ingredients to see if fresh
for ingredient in available_ingredients:
    if is_ingredient_fresh(fresh_id_ranges, ingredient):
        total_fresh_ingredients += 1

print(f"Total fresh ingredients is: {total_fresh_ingredients}")
