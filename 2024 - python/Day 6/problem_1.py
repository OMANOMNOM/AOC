def read_map():
    file = open("2024\\Day 6\\test_input_1.txt", "r")
    matrix = list()
    for row in file:
        temp = list()
        for chars in row.strip():
            temp.append(chars)
        matrix.append(temp)

    return matrix

def get_init_guard_pos():
    for row in range(0,len(matrix)):
        for symbol in guard:
            for index in range(0,len(matrix[row])):
                if matrix[row][index] in symbol:
                    guard_pos = [row, index]
                    guard_cur_symbol = matrix[row][index]
                    return guard_pos, guard_cur_symbol    

def debug_print(matrix):
    file = open("2024\\Day 6\\debug_input_1.txt", "w")
    for row in matrix:
        s_row = ""
        for column in row:
            s_row = s_row + str(column) 
        s_row = s_row + "\n"
        file.write(s_row)
    file.close()

matrix = read_map()
guard = ["^", ">", "v", "<"]
guard_fwd = {"^": [-1,0], ">":[0,1], "v": [1,0], "<": [0,-1]}
guard_pos = None
guard_cur_symbol = ""
traversed_positions = set()
guard_pos, guard_cur_symbol = get_init_guard_pos()
traversed_positions.add(str(guard_pos[0]) + "," +  str(guard_pos[1]))
# Navigate
is_done = False
while(not is_done):
    # If the something in front
    # get forward direction
    guard_current_forward_vec = guard_fwd[guard_cur_symbol]
    if matrix[guard_pos[0] + guard_current_forward_vec[0]][guard_pos[1]  + guard_current_forward_vec[1]] == "#":
        # turn 90
        guard_cur_symbol = guard[(guard.index(guard_cur_symbol) + 1) % 4]
        #debug_print(matrix)
    else:
        # Step forward
        traversed_positions.add(str(guard_pos[0]) + "," + str(guard_pos[1]))
        matrix[guard_pos[0]][guard_pos[1]] = "X"
        guard_pos = [guard_pos[0] + guard_current_forward_vec[0],guard_pos[1]  + guard_current_forward_vec[1]]
        next_turn_pos = [guard_pos[0] + guard_current_forward_vec[0],guard_pos[1]  + guard_current_forward_vec[1]]
        if next_turn_pos[0] < 0 or next_turn_pos[1] < 0 or next_turn_pos[0] >= len(matrix) or next_turn_pos[1] >= len(matrix[0]):
            is_done = True
            matrix[guard_pos[0]][guard_pos[1]] = guard_cur_symbol
            traversed_positions.add(str(guard_pos[0]) + "," + str(guard_pos[1]))
            debug_print(matrix)
            break
        matrix[guard_pos[0]][guard_pos[1]] = guard_cur_symbol
        
print(len(traversed_positions ))