# read test.txt

file = open("test.txt")
for lines in file:
    print(lines[0])
file.close()
