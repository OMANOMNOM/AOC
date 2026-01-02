def traverse_tree(start_pos, board):
    current_pos = start_pos
    total_splits = 0
    # else:
    #     pass
    # whilst not blocked
    is_traverseing_down = True
    while(is_traverseing_down):
        current_pos[0] += 1
        if (current_pos[0] >= len(board)):
            return 0
        if (board[current_pos[0]][current_pos[1]] == "^"):
            total_splits += 1
            total_splits += traverse_tree([current_pos[0], current_pos[1]-1], board)
            total_splits += traverse_tree([current_pos[0], current_pos[1]+1], board)
            is_traverseing_down = False
        elif (board[current_pos[0]][current_pos[1]] == "|"):
            return 0
        else:
            board[current_pos[0]] = board[current_pos[0]][: current_pos[1]] +"|" + board[current_pos[0]][current_pos[1]+ 1: ]
    return total_splits

# Read in file and return a 2d array of board
with open(r"C:\Projects\Code\AOC\2025 - python\day-7\problem-1.txt") as file:
    board = list()
    for line in file:
        board.append(line.strip())


start_pos = None
for line_index in range(len(board)):
    if "S" in board[line_index]:
        for column_index in range(len(board[line_index])):
            if board[line_index][column_index] == "S":
                start_pos = (line_index, column_index)

cur_pos = [start_pos[0], start_pos[1]]

total_splits = traverse_tree(cur_pos, board)
print(f"total number of spilts is: {total_splits}")
pass
