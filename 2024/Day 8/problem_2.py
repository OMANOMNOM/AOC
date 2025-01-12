from itertools import combinations


# Read in input
file = open("2024\Day 8\\input_1.txt", "r")
input_file = list()
for row in file:
    input_file.append(row)

def get_antenna_pos(input_file):
    antenna = dict()
    for row in range(0,len(input_file)):
        for column in range(0,len(input_file[0])-1):
            if input_file[row][column].isdigit() or input_file[row][column].isalpha():
                antenna_frequencies = None
                if input_file[row][column] in antenna:
                    antenna_frequencies = antenna[ input_file[row][column]]
                else:
                    antenna_frequencies = list()
                
                antenna_frequencies.append({"row" : row, "column" : column})
                antenna[input_file[row][column]]= antenna_frequencies
    return antenna

def debug_map_print(debug_file):
    file = open("2024\Day 8\\debug_test_input_1.txt", "w")
    for row in debug_file:
        file.write(row)

def is_valid_anitnode(antinode, input_file):
    if antinode["dy"] < 0 or (antinode["dy"] +1)  > len(input_file):
        return None
    if antinode["dx"] < 0 or (antinode["dx"] +1)  > len(input_file[0])-1:
        return None
    return f"{antinode["dy"]},{antinode["dx"]}"

antennas = get_antenna_pos(input_file)
unique_antinodes = set()
debug_file = input_file.copy()
for freq in antennas:
    freq_combinations = list(combinations(antennas[freq],2))
    for f_combination in freq_combinations:
        # calculate the line
        delta_y = f_combination[1]["row"] - f_combination[0]["row"]
        delta_x = f_combination[1]["column"] - f_combination[0]["column"]
        line_p0_to_p1 = {"dy": delta_y, "dx": delta_x}
        # Anitinode which is 2 from p0
        antinodes = list()
        
        max_search = max(len(input_file),len(input_file[0]))
        for i in range(0,(max_search//max(abs(line_p0_to_p1["dy"]), abs(line_p0_to_p1["dx"])) + 1)):
            if i == 0:
                antinodes.append({"dy" : f_combination[0]["row"], "dx" : f_combination[0]["column"]})
            antinodes.append({"dy" : (delta_y * i) + f_combination[0]["row"], "dx" : (delta_x  * i) + f_combination[0]["column"]})
            antinodes.append({"dy" : (delta_y * -i) + f_combination[0]["row"], "dx" : (delta_x  * -i) + f_combination[0]["column"]})
        for antinode in antinodes:
            position = is_valid_anitnode(antinode, input_file)
            if position is not None:
                unique_antinodes.add(position)
                temp_row = debug_file[antinode["dy"]]
                debug_file[antinode["dy"]] = temp_row[:antinode["dx"]] + "#" + temp_row[antinode["dx"]+1:] 
debug_map_print(debug_file)

print(f"The total number of antinodes is {len(unique_antinodes)}")


        