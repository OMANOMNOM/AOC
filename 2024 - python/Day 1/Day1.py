
# Read in row by row
    # append first number to first list and second to second list

# Sort both lists from smallest to largest. 
# Loop thorugh list by index, calculating distance
    # Append this distance to totol distance

a = list()
b = list()

f = open("2024\\Day 1\\input_1.txt", "r")
for x in f:
  a_input, b_input = x.split(maxsplit=2)
  a.append(a_input)
  b.append(b_input)

a.sort()
b.sort()
total_dist = 0
for i in range(0, len(a)):
  total_dist += abs(int(a[i]) - int(b[i]))

print(f"The total distance between the two lists is: {total_dist}")
