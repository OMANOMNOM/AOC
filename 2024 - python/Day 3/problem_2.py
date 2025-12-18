# import re 

# def get_search_indicies(pattern):
#         # Get positions of dos
#     search_result = re.search(pattern, line)
#     string_pos = list()
#     search_start = 0
#     indicies_total = 0
#     if pattern == "do\(\)":
#         string_pos.append(0)
#     while search_result is not None:
#         search_result = re.search(pattern, line[indicies_total:])
#         if search_result is not None:
#             indicies_total += search_result.start(0)
#             string_pos.append(indicies_total)
#             indicies_total += 1
#             print(indicies_total)
#     return string_pos

# def get_highest_index_below_value(index, cur_list):
#     # Input an index
#     # Loop through list, get store value which is below index, but higher than current value
#     cur_val = -1
#     for i in cur_list:
#         if i < index and i > cur_val:
#             cur_val = i
    
#     return cur_val

# # Main
# # Read in the entire file, row by row. 
# total_safe_reports = 0
# total_enabled = 0
# total_disabled = 0

# f = open("2024\\Day 3\\input_2.txt", "r")
# line = ""
# for l in f:
#     line += l
    
# do_cmd = get_search_indicies("do\(\)")
# dont_cmd = get_search_indicies("don't\(\)")

# for command in re.finditer("mul\(\d{1,3},\d{1,3}\)", line):
#     if get_highest_index_below_value(command.start(), do_cmd) > get_highest_index_below_value(command.start(), dont_cmd):
#         nums = re.findall("[0-9]+", line[command.start(): command.end()])
#         total_enabled += (int(nums[0]) * int(nums[1]))
#     else:
#         nums = re.findall("[0-9]+", line[command.start(): command.end()])
#         total_disabled += (int(nums[0]) * int(nums[1]))
# print(f"Total enabled is :{total_enabled}")   
# print(f"Total disabled is :{total_disabled}")  
# print(f"Total added together is {total_enabled + total_disabled}")
# print(f"We are off by {162813399 - (total_enabled + total_disabled)}") 
