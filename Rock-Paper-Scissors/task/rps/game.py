import random

file_name_append = open("rating.txt", "a")
file_name_read = open("rating.txt", "r")

name = input("Enter your name: ")
print("Hello, {}".format(name))
name_exists = None
for lines in file_name_read:
    if lines.startswith(name):
        name_exists = True
        split_lines = lines.split()
        score_map = {name: int(split_lines[1])}

if name_exists is not True:
    file_name_append.write(f"{name} 0")
    score_map = {name: 0}
else:
    # Print error?
    score_map = None

while True:
    random_num = random.randrange(1, 4)
    options = {1: "rock", 2: "paper", 3: "scissors"}
    computer_choice = options[random_num]
    answer = input()
    if answer == "!exit":
        print("Bye!")
        break

    if answer == "!rating":
        print(f"Your rating: {score_map[name]}")

    if answer == "scissors":
        if computer_choice == "rock":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "scissors":
            print(f"There is a draw ({computer_choice})")
            score_map[name] += 50
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
            score_map[name] += 100
    elif answer == "rock":
        if computer_choice == "paper":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "rock":
            print(f"There is a draw ({computer_choice})")
            score_map[name] += 50
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
            score_map[name] += 100
    elif answer == "paper":
        if computer_choice == "scissors":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "paper":
            print(f"There is a draw ({computer_choice})")
            score_map[name] += 50
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
            score_map[name] += 100
    else:
        print("Invalid input")
