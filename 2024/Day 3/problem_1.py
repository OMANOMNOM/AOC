import re 

# Read in the entire file, row by row. 
f = open("2024\Day 3\\input_1.txt", "r")

total_safe_reports = 0
total = 0
for line in f:
    # split at every mul
    commands = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
   
        # extract both numbers
    for command in commands:
        nums = re.findall("[0-9]+", command)
        total += (int(nums[0]) * int(nums[1]))
        

print(total)
