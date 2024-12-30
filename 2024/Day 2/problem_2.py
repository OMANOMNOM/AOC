def check_report(reports):
    is_decreasing = False
    is_increasing = False
    is_lvl_diff_valid = True

    for index in range(0,len(reports)-1):
        l_val = int(reports[index])
        r_val = int(reports[index + 1])
        if (l_val < r_val):
            is_increasing = True
        if (l_val > r_val):
            is_decreasing = True
        if abs(l_val - r_val) < 1 or abs(l_val - r_val) > 3:
            is_lvl_diff_valid = False
    
    if is_decreasing and is_increasing:
        return 0
    if is_decreasing and is_lvl_diff_valid or is_increasing and is_lvl_diff_valid:
        return 1
    else:
        return 0


f = open("2024\Day 2\\input_1.txt", "r")

total_safe_reports = 0
for x in f:
    reports = x.split()
    
    if check_report(reports) == 1:
        total_safe_reports += 1
        continue
    else:
        for attempts in range(0,len(reports)):
            modified_list = reports.copy()
            modified_list.pop(attempts)
            if check_report(modified_list) == 1:
                total_safe_reports +=1
                break
     


    

print(total_safe_reports)