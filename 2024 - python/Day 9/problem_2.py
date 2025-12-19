# Read in input
IS_TEST = False

if IS_TEST:
    file = open("2024\\Day 9\\test_input_1.txt", "r")
else:
    file = open("2024\\Day 9\\input_1.txt", "r")
input_file = list()
for row in file:
    input_file.append(row)

def expand_disk(input_file):
    """Returns a single string with the expanded disk"""
    expanded_string = list()
    is_space = False
    id = 0
    for element in input_file[0]:
        if element == "\n":
            continue
        ouput_char = ""
        if is_space:
            output_char = "."
        else:
            output_char = str(id)
        for length in range(0,int(element)):
            expanded_string.append(output_char)

        if is_space is False:
            is_space = True
        else:
            is_space = False
            id += 1
    print_list(expanded_string)
    write_list(expanded_string)
    return expanded_string

def print_list(disk):
    output = ""
    for i in range(0,len(disk)):
        output += disk[i] + ","
    print(output)


def write_list(disk, sort = None):
    file = None 
    if sort:
        file = open("2024\\Day 9\\debug_compress.txt", "w")
    else:
        file = open("2024\\Day 9\\debug_expand.txt", "w")
    output = ""
    for i in range(0,len(disk)):
        output += disk[i] + ","
    file.write(output)
    file.close()

def sort_disk_contiguous(expanded):
    """ removes all the empty space 

    Args:
        expanded (_type_): _description_
    """

    is_sorted = False
    print_count = 0
    moved_ids = list()
    while(not is_sorted):
        
        cur_file_id = expanded[len(expanded )-1]
        cur_file_size = 0
        list_offset = 0
        moved_files = list()
        # Loop from highest to lowest file ID
        for i in range(len(expanded)-1, -1, -1):
            # if list_offset > 0:
            #     list_offset -= 1
            #     continue
            if expanded[i] == "." and cur_file_id == ".": # space continuation 
                continue
            elif expanded[i] != "." and cur_file_id == expanded[i]: # continuation
                # if same file
                cur_file_size +=1
            elif cur_file_id != expanded[i]:
                if cur_file_id != "." and cur_file_id not in moved_files:
                    expanded = move_to_first_free_space(cur_file_id, cur_file_size, i, expanded)
                    list_offset = cur_file_size
                    moved_files.append(cur_file_id)
                cur_file_id = expanded[i]
                cur_file_size = 1
            #print_list(expanded)
        is_sorted = True
        # print_count += 1
        # if print_count % 50 == 0:
        #     write_list(expanded, True)
    return expanded

def move_to_first_free_space(file_id, file_size, cur_position, arr):
    # Travel along the loop up until the current position 
    space_size = 0
    for i in range(0, len(arr)):
        if arr[i] == ".":
            if i > cur_position:
                return arr
            if space_size > 0:
                space_size += 1
            else:
                space_pos = i
                space_size = 1
            if space_size == file_size:
                arr = arr[:space_pos] + arr[cur_position+ 1:cur_position+file_size+1] + arr[space_pos+space_size  : cur_position + 1] + arr[space_pos : space_pos + space_size] + arr[cur_position + file_size+ 1 :]
                print_list(arr)
                return arr
        else:
            space_size = 0
    return arr
        # If space
                # If length is greater or equal to file length 
                    # Preform swap. 
    #return swapped array. 

def check_test_value(compressed):
    if compressed ==  "00992111777.44.333....5555.6666.....8888..":
        print("Test passed")

def calculate_checksum(compressed):
    total = 0
    for i in range(0,len(compressed)-1):
            if compressed[i] != ".":
                total += i * int(compressed[i])
    return total


expanded =  expand_disk(input_file)


print("--- Sorted ---")
final_disk = sort_disk_contiguous(expanded)

if IS_TEST:
    check_test_value(final_disk)
print(f"The checksum is: {calculate_checksum(final_disk)}")