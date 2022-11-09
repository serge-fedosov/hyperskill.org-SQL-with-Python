file = open('test.fastq', 'r')
count = 0
for line in file:
    print(line)
    if count == 3:
        break

file.close()
