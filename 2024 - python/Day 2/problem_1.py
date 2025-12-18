

f = open("2024\Day 2\\input_1.txt", "r")

total_safe_reports = 0
for x in f:
    a_input = x.split()
    is_decreasing = False
    is_increasing = False
    is_lvl_diff_valid = True
    
    for index in range(0,len(a_input)-1):
        l_val = int(a_input[index])
        r_val = int(a_input[index + 1])
        if (l_val < r_val):
            is_increasing = True
        if (l_val > r_val):
            is_decreasing = True
        if abs(l_val - r_val) < 1 or abs(l_val - r_val) > 3:
            is_lvl_diff_valid = False
    
    if is_decreasing and is_increasing:
        continue
    if is_decreasing and is_lvl_diff_valid or is_increasing and is_lvl_diff_valid:
        total_safe_reports += 1

print(total_safe_reports)