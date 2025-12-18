def create_matix():
    f = open("2024\Day 4\\input_1.txt", "r")
    matrix = list()
    for line in f:
        matrix.append(line)
    return matrix

def check_for_cross(start, target_matrix):
    for row in range(-1,2):
        for column in range(-1,2):
            if row + start[0] < 0 or row + start[0] > len(matrix) - 1 or column + start[1] < 0 or column + start[1] > len(matrix[0]) -1:    
                return False
            if target_matrix[row+1][column+1] == ".":
                continue
            if target_matrix[row+1][column+1] != matrix[start[0] + row][start[1] + column]:
                return False
    return True

matrix = create_matix()
target = "XMAS"
tree = [[["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]],
        [["M", ".", "M"], [".", "A", "."], ["S", ".", "S"]],
        [["S", ".", "S"], [".", "A", "."], ["M", ".", "M"]],
        [["S", ".", "M"], [".", "A", "."], ["S", ".", "M"]],
        ]


matches = 0
for row in range(0,len(matrix)):
    for column in range(0,len(matrix[row])):
        print(matrix[row][column])
        for combinations in tree:
            if check_for_cross([row, column], combinations):
                matches += 1
            

print(f"Total number of matches is {matches}")
# Read in line by line
    # Create a 2d Array

