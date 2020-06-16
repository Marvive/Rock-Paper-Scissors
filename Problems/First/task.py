# read test_file.txt
file = open("test_file.txt", encoding='utf-16')
for i in file:
    print(i)
    break

file.close()
