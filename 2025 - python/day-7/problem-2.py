def traverse_tree(start_pos, board):
    current_pos = start_pos
    
    is_traverseing_down = True
    while(is_traverseing_down):
        current_pos[0] += 1
        if tuple(current_pos) in MEM:
            return MEM[tuple(current_pos)]
        if (current_pos[0] >= len(board)):
            return 1
        if (board[current_pos[0]][current_pos[1]] == "^"):
            cached_traversal =  traverse_tree([current_pos[0], current_pos[1]-1], board) + traverse_tree([current_pos[0], current_pos[1]+1], board)
            MEM[tuple(current_pos)] = cached_traversal
            return cached_traversal
    return 


def read_board_and_start_pos():
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
    return start_pos, board

start_pos, board = read_board_and_start_pos()
MEM = dict()
combinations = list(start_pos)
total_traversed = traverse_tree(list(start_pos), board)
print(f"Total traversed is : {total_traversed}")
