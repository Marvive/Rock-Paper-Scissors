numbers = [1234, 5678, 90]
num_string = str(numbers)
# save this list in `file_with_list.txt`
file_name = open("file_with_list.txt", "w")

file_name.write(num_string)

file_name.close()
