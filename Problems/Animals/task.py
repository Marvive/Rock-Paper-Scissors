# read animals.txt
# and write animals_new.txt
file = open("animals.txt")
new_file = open("animals_new.txt", "w")

for i in file:
    new_file.write(i.rstrip() + " ")
new_file.close()
file.close()
