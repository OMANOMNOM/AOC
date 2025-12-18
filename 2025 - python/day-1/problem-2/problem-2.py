from tracemalloc import start


def apply_move(cur_num, direction, distance):
    if direction == 'R':
        cur_num += (distance % 100)
    elif direction == 'L':
        cur_num -= (distance % 100)
    if cur_num > 99:
        cur_num = 0 + (cur_num % 100)
    elif cur_num < 0:
        cur_num = (100 - abs(cur_num ))
    return cur_num

def count_zeros_hit(start_num, direction, distance, end_num):
    zeros_hit = 0
    
    zeros_hit += distance // 100
    if start_num == 0:
        return zeros_hit
    elif start_num != 0 and end_num == 0:
        zeros_hit += 1
    elif direction == 'R' and start_num > end_num:
        zeros_hit += 1
    elif direction == 'L' and start_num < end_num:
        zeros_hit += 1
    return zeros_hit 

total_zeros = 0
cur_num = 50
for line in open(r"C:\Projects\Code\AOC\2025 - python\day-1\problem-2\problem-2.txt"):
    start_num = cur_num
    direction = line[0]
    distance = int(line[1:].strip())
    cur_num = apply_move(cur_num, direction, distance)
    passed_zero = count_zeros_hit(start_num,direction, distance, cur_num)
    print(f"{cur_num} : {passed_zero}")
    total_zeros += passed_zero
    
print(f"Total times at 0: {total_zeros}")

