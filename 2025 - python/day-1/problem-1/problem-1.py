def apply_move(cur_num, direction, distance):
    if direction == 'R':
        cur_num += (distance % 100)
    elif direction == 'L':
        cur_num -= (distance % 100)
    if cur_num > 99:
        cur_num = 0 + (cur_num % 100)
    elif cur_num < 0:
        cur_num = (100 - abs(cur_num ))
    print(f"{cur_num}")
    return cur_num

total_zeros = 0
cur_num = 50
for line in open("problem-1.txt"):
    direction = line[0]
    distance = int(line[1:].strip())
    cur_num = apply_move(cur_num, direction, distance)
    if cur_num == 0:
        total_zeros += 1
    
print(f"Total times at 0: {total_zeros}")

# read in the example.txt
