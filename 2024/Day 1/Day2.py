a = list()
b = list()

f = open("2024\Day 1\input_1.txt", "r")
for x in f:
  a_input, b_input = x.split(maxsplit=2)
  a.append(a_input)
  b.append(b_input)

total = 0
for i in range(0, len(a)):
  occurances = b.count(a[i])
  total += int(a[i]) * occurances

print(f"The new final total is {total}")