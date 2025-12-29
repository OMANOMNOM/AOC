# create 2d array of board
board = []


def check_paper(row, col, board):
    adjacent_papers = 0
    # Check all 8 directions for adjacent cells
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for dr, dc in directions:
        row_check = row + dr
        col_check = col + dc    
        if row_check < 0 or row_check >= len(board) or col_check < 0 or col_check >= len(board[0]):
            continue
        if board[row_check][col_check] == "@":
            adjacent_papers += 1
    if adjacent_papers < 4:
        print(f"Paper at ({row}, {col}) is unstable with {adjacent_papers} adjacent papers.")
        return True
    return False

with open(r"C:\Projects\Code\AOC\2025 - python\day-4\problem-1.txt", "r") as file:
    for line in file:
        board.append(line.strip())

accessable_papers = 0
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == "@":
            if check_paper(row, col, board):
                accessable_papers += 1
        
print(f"Total accessable papers: {accessable_papers}")
        
        
    