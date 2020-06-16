# read sums.txt
file = open("sums.txt")
for i in file:
    num = i.split()
    print(sum(map(int, num)))
file.close()