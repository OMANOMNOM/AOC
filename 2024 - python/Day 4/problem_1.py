

def create_matix():
    f = open("2024\Day 4\\input_1.txt", "r")
    matrix = list()
    for line in f:
        matrix.append(line)
    return matrix

def check_for_word(start, direction):
    for indxes in range(0,len(target)):
        char = target[indxes]
        movement = direction[indxes]
        if start[0] + movement[0] < 0 or start[0] + movement[0] > len(matrix[0]) -2 or start[1] + movement[1] < 0 or start[1] + movement[1] > len(matrix[0]) -2:
            return False
        else:
            check_square = matrix[start[0] + movement[0]][start[1] + movement[1]]
        if check_square != char:
            return False
        
    return True

matrix = create_matix()
target = "XMAS"
HORIZONTAL_FORWARD = [[0,0],[0,1],[0,2],[0,3]]
HORIZONTAL_BACKWARD = [[0,0],[0,-1],[0,-2],[0,-3]]
VERTICAL_UP = [[0,0],[-1,0],[-2,0],[-3,0]]
VERTICAL_DOWN = [[0,0],[1,0],[2,0],[3,0]]
DIAGONAL_NW = [[0,0],[-1,-1],[-2,-2],[-3,-3]]
DIAGONAL_NE = [[0,0],[-1,1],[-2,2],[-3,3]]
DIAGONAL_SE = [[0,0],[1,1],[2,2],[3,3]]
DIAGONAL_SW = [[0,0],[1,-1],[2,-2],[3,-3]]


matches = 0
for row in range(0,len(matrix)):
    for column in range(0,len(matrix[row])):
        print(matrix[row][column])
        if check_for_word([row,column], HORIZONTAL_FORWARD):
            print("True")
            matches += 1
        if check_for_word([row,column], HORIZONTAL_BACKWARD):
            print("True")
            matches += 1
        if check_for_word([row,column], VERTICAL_UP):
            print("True")
            matches += 1
        if check_for_word([row,column], VERTICAL_DOWN):
            print("True")
            matches += 1
        if check_for_word([row,column], DIAGONAL_NW):
            print("True")
            matches += 1
        if check_for_word([row,column], DIAGONAL_NE):
            print("True")
            matches += 1
        if check_for_word([row,column], DIAGONAL_SE):
            print("True")
            matches += 1
        if check_for_word([row,column], DIAGONAL_SW):
            print("True")
            matches += 1
            

print(f"Total number of matches is {matches}")
# Read in line by line
    # Create a 2d Array

# Go through the array.
    # Check horionztal
    # Check vertical
    # Check Diagonal

