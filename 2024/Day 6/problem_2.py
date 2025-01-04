def read_map():
    file = open("2024\Day 6\\input_1.txt", "r")
    matrix = list()
    for row in file:
        temp = list()
        for chars in row.strip():
            temp.append(chars)
        matrix.append(temp)

    return matrix

def get_init_guard_pos(matrix):
    for row in range(0,len(matrix)):
        for symbol in guard:
            for index in range(0,len(matrix[row])):
                if matrix[row][index] in symbol:
                    guard_pos = [row, index]
                    guard_cur_symbol = matrix[row][index]
                    return guard_pos, guard_cur_symbol    

def debug_print(matrix, f_number = 1):

    file = open("2024\Day 6\\debug_input_" + str(f_number) + ".txt", "w")
    for row in matrix:
        s_row = ""
        for column in row:
            s_row = s_row + str(column) 
        s_row = s_row + "\n"
        file.write(s_row)
    file.close()

def traverse_path(guard, guard_fwd, guard_pos, guard_cur_symbol, traversed_positions, guard_current_forward_vec, matrix):
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
                #debug_print(matrix)
                break
            matrix[guard_pos[0]][guard_pos[1]] = guard_cur_symbol

matrix = read_map()
guard = ["^", ">", "v", "<"]
guard_fwd = {"^": [-1,0], ">":[0,1], "v": [1,0], "<": [0,-1]}
guard_pos = None
guard_cur_symbol = ""
traversed_positions = set()
guard_pos, guard_cur_symbol = get_init_guard_pos(matrix)
traversed_positions.add(str(guard_pos[0]) + "," +  str(guard_pos[1]))
guard_current_forward_vec = None
# Navigate


traverse_path(guard, guard_fwd, guard_pos, guard_cur_symbol, traversed_positions, guard_current_forward_vec, matrix)

total_loop = 0
for obstacle_pos in traversed_positions:
    modified_matrix = read_map()
    obstacles = ["#", "0"]
    newly_traversed = set()
    guard_pos, guard_cur_symbol = get_init_guard_pos(modified_matrix)
    init_position = guard_pos.copy()
    if modified_matrix[int(obstacle_pos.split(",")[0])][int(obstacle_pos.split(",")[1])] is not "^":
        modified_matrix[int(obstacle_pos.split(",")[0])][int(obstacle_pos.split(",")[1])] = "0"
    else:
        continue
    # Run the traversal function
    is_done = False
    while(not is_done):
        # If the something in front
        # get forward direction
        guard_current_forward_vec = guard_fwd[guard_cur_symbol]
        if modified_matrix[guard_pos[0] + guard_current_forward_vec[0]][guard_pos[1]  + guard_current_forward_vec[1]] in obstacles:
            # turn 90
            guard_cur_symbol = guard[(guard.index(guard_cur_symbol) + 1) % 4]
            modified_matrix[guard_pos[0]][guard_pos[1]] = "+"
            #debug_print(modified_matrix)

        else:
            # Step forward
            if modified_matrix[guard_pos[0]][guard_pos[1]] != "+" and not (guard_pos[0] == init_position[0] and guard_pos[1] == init_position[1]):
                modified_matrix[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = [guard_pos[0] + guard_current_forward_vec[0],guard_pos[1]  + guard_current_forward_vec[1]]
            next_turn_pos = [guard_pos[0] + guard_current_forward_vec[0],guard_pos[1]  + guard_current_forward_vec[1]]
            if next_turn_pos[0] < 0 or next_turn_pos[1] < 0 or next_turn_pos[0] >= len(modified_matrix) or next_turn_pos[1] >= len(modified_matrix[0]):
                is_done = True
                modified_matrix[guard_pos[0]][guard_pos[1]] = guard_cur_symbol
                break
            modified_matrix[guard_pos[0]][guard_pos[1]] = guard_cur_symbol
            if str(guard_pos[0]) + "," + str(guard_pos[1])  + "," + str(guard_cur_symbol) in newly_traversed:
                # we have a loop
                #print("We have a loop")
                #debug_print(modified_matrix,total_loop)
                total_loop += 1
                break
            newly_traversed.add(str(guard_pos[0]) + "," + str(guard_pos[1])  + "," + str(guard_cur_symbol)) # This line needs moving down

print(total_loop)
        # Run the traversal function. 
            # If at any point we end up at a traversal poitn with same vector then we know we're in a loop 
            # Continue for 20k iterations. 
