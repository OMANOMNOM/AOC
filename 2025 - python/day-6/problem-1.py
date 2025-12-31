# read in file 
    # Loop through each line putting each line into a 2d list.
from re import split


data = list()
with open(r"C:\Projects\Code\AOC\2025 - python\day-6\problem-1.txt") as file:
    for line in file:
        elements = split(r"\s+", line.strip(),)
        for index in range(len(elements)):
            if len(data)-1 < index:
                if elements[index].isdigit():
                    data.append([(int(elements[index]))])
                else:
                    data.append([(elements[index])])
            else:
                if elements[index].isdigit():
                    data[index].append(int(elements[index]))
                else:
                    data[index].append(elements[index])



# Go through the list performing the opeartion
# add up the total
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

