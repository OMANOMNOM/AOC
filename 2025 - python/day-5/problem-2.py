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

def calc_total_fresh_ingredients(fresh_id_ranges):
    total_ids = 0
    for id_range in fresh_id_ranges:
        total_ids += id_range["end"]+1 - id_range["start"]
    print(f"The total Id range is {total_ids}")

def condense_ranges(fresh_id_ranges):
    condensed_ranges = list()
    adjustment_made = False
    for id_range in fresh_id_ranges:
        # Put first range in manually.
        if len(condensed_ranges) == 0:
            condensed_ranges.append(id_range)
            continue
        # Does range intersect with condensed range?
        is_intersects = False
        for condensed_range in condensed_ranges:
            # If range full insiide of condensed range, don't do anything
            if id_range["start"] >= condensed_range["start"] and id_range["end"] <= condensed_range["end"]:
                is_intersects = True
                break
            # if range is partially intersecting condensed range extend, condensed range
            elif id_range["start"] >= condensed_range["start"] and id_range["start"] <= condensed_range["end"] and id_range["end"] > condensed_range["end"]:
                condensed_range["end"] = id_range["end"]
                adjustment_made = True
                is_intersects = True
                break
            elif id_range["start"] < condensed_range["start"] and id_range["end"] >= condensed_range["start"] and id_range["end"] <= condensed_range["end"]:
                condensed_range["start"] = id_range["start"]
                adjustment_made = True
                is_intersects = True
                break 
            elif id_range["start"] < condensed_range["start"] and id_range["end"] > condensed_range["end"]:
                condensed_range["start"] = id_range["start"]
                condensed_range["end"] = id_range["end"] 
                adjustment_made = True
                is_intersects = True 
                break
        if not is_intersects:
            condensed_ranges.append({"start": id_range["start"], "end": id_range["end"]})
            adjustment_made = True
    return condensed_ranges, adjustment_made

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
                # process freshIDs 
        else:
            available_ingredients.append(int(line))
            #process available ingredient IDs


# total_fresh_ingredients = 0
# # Loop through available ingredients to see if fresh
# for ingredient in available_ingredients:
#     if is_ingredient_fresh(fresh_id_ranges, ingredient):
#         total_fresh_ingredients += 1

# print(f"Total fresh ingredients is: {total_fresh_ingredients}")

still_condensing = True
while(still_condensing):
    condensed_ranges, still_condensing = condense_ranges(fresh_id_ranges)
    if len(condensed_ranges) == len(fresh_id_ranges):
        break
    fresh_id_ranges = condensed_ranges
calc_total_fresh_ingredients(fresh_id_ranges)
pass
# Finally get the len
            
