file = open('input.txt', 'r')
count = 0
for line in file:
    if line == "summer\n":
        count += 1

file.close()
print(count)
