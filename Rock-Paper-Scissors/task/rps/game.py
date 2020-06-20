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
    score_map = {name: 0}

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
                file_name_append.write("\n")
                file_name_append.write(f"{name} {str(score_map[name])}")
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
    choice_map = {}
    counter = 0
    num_of_styles = len(game_style)
    for choice in game_style:
        choice_map[counter] = choice
        counter += 1
    while True:
        random_num = random.randrange(0, len(game_style))
        computer_choice = choice_map[random_num]
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
                file_name_append.write("\n")
                file_name_append.write(name + " " + str(score_map[name]))
            print("Bye!")
            break

        if answer == "!rating":
            print(f"Your rating: {score_map[name]}")
            continue

    #     Check results
    # Each choice should beat half of the options - 1
        if answer in choice_map.values():
            print("Option Valid")
            answer_key = game_style.index(answer)
            if answer_key == random_num:
                print(f"There is a draw ({computer_choice})")
                score_map[name] += 50
                continue

            strong_or_weak_choice_possibilities = num_of_styles // 2
            # strong_list = [x for x + answer_key in range(strong_choice_possibilities)]
            strong_list = []
            weak_list = []
            counter = 1
            weak_counter = 1
            weak_counter_negative = -1
            passed_strong = False
            for i in range(strong_or_weak_choice_possibilities):
                if counter + answer_key >= num_of_styles and passed_strong is False:
                    counter *= 0
                    strong_list.append(choice_map[counter])
                    passed_strong = True
                elif passed_strong:
                    counter += 1
                    strong_list.append(choice_map[counter])
                else:
                    strong_list.append(choice_map[counter + answer_key])
                    counter += 1
                if answer_key - weak_counter >= 0:
                    weak_list.append(choice_map[answer_key - weak_counter])
                    weak_counter += 1
                else:
                    weak_list.append(game_style[weak_counter_negative])
                    weak_counter_negative -= 1
            # print(strong_or_weak_choice_possibilities)
            # print(answer_key)
            # print(strong_list)
            # print(weak_list)
            if computer_choice in strong_list:
                print(f"Sorry, but computer chose {computer_choice}")
            else:
                print(f"Well done. Computer chose {computer_choice} and failed")
                score_map[name] += 100

        else:
            print("Invalid input")
    # print(choice_map)

# Strong choice = (len_choices // 2) + answer_key


file_name_read.close()
file_name_append.close()
