import random
import fileinput

file_name_append = open("rating.txt", "a")
file_name_read = open("rating.txt", "r")

name = input("Enter your name: ")
print("Hello, {}".format(name))
name_exists = None
rating_dictionary = {}
for lines in file_name_read:
    if lines.startswith(name):
        name_exists = True
        split_lines = lines.split()
        old_line = f"{name} {split_lines[1]}"
        score_map = {name: int(split_lines[1])}
    elif "0" in lines:
        split_lines = lines.split()
        rating_dictionary[split_lines[0]] = split_lines[1]
file_name_read.close()

if name_exists is not True:
    # file_name_append.write(f"{name} 0\n")
    score_map = {name: 0}
    # file_name_append.close()

game_style = input().split(",")
print("Okay let's start")

if not game_style[0]:
    while True:
        random_num = random.randrange(1, 4)
        options = {1: "rock", 2: "paper", 3: "scissors"}
        computer_choice = options[random_num]
        answer = input()
        if answer == "!exit":
            if name_exists:
                for lines in fileinput.input('rating.txt', inplace=True):
                    if name in lines:
                        lines = name + " " + str(score_map[name])
                        print(lines.rstrip('\r\n'))
                    elif "0" in lines:
                        print(lines.rstrip('\r\n'))
            else:
                file_name_append.write(name + " " + str(score_map[name]))
            print("Bye!")
            break

        if answer == "!rating":
            print(f"Your rating: {score_map[name]}")
            continue

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
else:
    print(game_style)

file_name_read.close()
file_name_append.close()
