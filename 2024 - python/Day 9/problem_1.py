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

def sort_disk(expanded):
    """ removes all the empty space 

    Args:
        expanded (_type_): _description_
    """

    is_sorted = False
    print_count = 0
    # whilst the first space has a lower index than the last piece that isn't a space
    while(not is_sorted):
        last_id_pos = None
        # take the last id_val
        for i in range(len(expanded)-1, -1, -1):
            if expanded[i] != ".":
                last_id_pos = i
                break
        stop_pos = None
        for j in range(0,len(expanded)):
            if expanded[j] == ".":
                stop_pos = j
                break
        if j == last_id_pos + 1:
            is_sorted = True
            return expanded
        
        # Replace the space char
        temp = expanded[last_id_pos]
        expanded = expanded[:stop_pos] + list([expanded[last_id_pos]]) + expanded[stop_pos + 1:]
        # Replace the element
        expanded = expanded[:last_id_pos ] + list(".") + expanded[last_id_pos + 1:]

        print_count += 1
        if print_count % 50 == 0:
            write_list(expanded, True)

def check_test_value(compressed):
    if compressed ==  "0099811188827773336446555566..............":
        print("Test passed")

def calculate_checksum(compressed):
    total = 0
    for i in range(0,len(compressed)-1):
            if compressed[i] != ".":
                total += i * int(compressed[i])
    return total


expanded =  expand_disk(input_file)


print("--- Sorted ---")
final_disk = sort_disk(expanded)

if IS_TEST:
    check_test_value(final_disk)
print(f"The checksum is: {calculate_checksum(final_disk)}")