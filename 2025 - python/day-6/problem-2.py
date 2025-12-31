# read in file 
    # Loop through each line putting each line into a 2d list.
from re import split
import re 
def read_in_problems():
    data = dict()
    with open(r"C:\Projects\Code\AOC\2025 - python\day-6\problem-1.txt") as file:
        for line in file:
            for char_index in range(len(line.strip())):
                if char_index in data:
                    data[char_index] = data[char_index] + line[char_index]
                else:
                    data[char_index] = line[char_index]

    # Loop through data of numbers and operators
    processed_data = list()
    for keys, elements in data.items():
        if "*" in elements or "+" in elements:
            tmp = list()
            if "*" in elements:
                tmp.append("*")
            if "+" in elements:
                tmp.append("+")
        match = re.search(r"\d+", elements)
        if match:
            tmp.append(int(match.group()))
        if elements.isspace():
            processed_data.append(tmp)
    processed_data.append(tmp)
    return processed_data



def solve_problems(data):
    total = 0 
    for problem in data:
        sum = 0
        if "+" in problem:
            for element in problem:
                if isinstance(element,int):
                    sum += element  
        elif "*" in problem:
            for element in problem:
                if isinstance(element,int):
                    if sum == 0:
                        sum += element
                    else:
                        sum *= element
        total += sum 

    print(f"Total of all problems is :{total}")

data = read_in_problems()
solve_problems(data)