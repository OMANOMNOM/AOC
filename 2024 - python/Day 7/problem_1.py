from itertools import combinations, permutations, product


file = open("2024\Day 7\\input_1.txt", "r")
total_total = 0
for line in file:
    test_answer, test_input = line.split(":")
    test_inputs = test_input.split()
    operations = len(test_inputs) - 1
    perm = list(product(["m","a","||"], repeat=operations))
    for operators in perm:
        total = None
        # Loop throug indexes of test inputs
        for index in range(0,len(test_inputs)-1):
            if total is None:
                a = int(test_inputs[index]) 
            else:
                a = total    
            b = int(test_inputs[index + 1])
            
                # Get operators
            if operators[index] == "m":
                total = a * b
            if operators[index] == "a":
                total = a + b
            if operators[index] == "||":
                temp = str(a) + str(b)
                total = int(temp)
                #add 
        if total == int(test_answer):
            total_total += total
            print(line)
            break    

print(total_total)




        