# Read each line and store as bank
with open(r"C:\Projects\Code\AOC\2025 - python\day-3\problem-1.txt") as f:
    total_joltage = 0
    for line in f:
        bank = line.strip()
        cur_largest = 0
        for joltage in range(len(bank) - 1):
            first_num = int(bank[joltage])
            for j in range(joltage+1, len(bank)):
                second_num = int(bank[j])
                on_batteries = (first_num * 10) + second_num
                if on_batteries > cur_largest:
                    cur_largest = on_batteries
        print(f"largest number for bank {bank} is {cur_largest}")
        total_joltage += cur_largest
    print(f"total joltage from all banks is {total_joltage}")
                
            

# Loop through each bank
  # Get the two largest numbers in pos 0 to n-1
    # Get the two largest numbers in pos 1 to n
 