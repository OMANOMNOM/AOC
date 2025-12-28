import math
def calc_largest_joltage(bank_sub_str, ith_digit : str) -> int:
    # return largest digit formed between the start of the substring and 
    # the -ith digit in the substring
    cur_largest = 0
    remaining_substr = None
    for joltage in range(len(bank_sub_str) - (12-ith_digit)):
        if int(bank_sub_str[joltage]) > cur_largest:
            cur_largest = int(bank_sub_str[joltage])
            remaining_substr = bank_sub_str[joltage+1:]
    # recusive termination 
    if ith_digit != 12:
        next_largest = calc_largest_joltage(remaining_substr, ith_digit + 1)
        cur_largest = (cur_largest * math.pow(10, (12 - ith_digit))) + next_largest
    return cur_largest

# Read each line and store as bank
with open(r"C:\Projects\Code\AOC\2025 - python\day-3\problem-1.txt") as f:
    total_joltage = 0
    for line in f:
        bank = line.strip()
        cur_largest = calc_largest_joltage(bank, 1)
        print(f"largest number for bank {bank} is {cur_largest}")
        total_joltage += cur_largest
    print(f"total joltage from all banks is {total_joltage}")
                
            

# Loop through each bank
  # Get the two largest numbers in pos 0 to n-1
    # Get the two largest numbers in pos 1 to n
 