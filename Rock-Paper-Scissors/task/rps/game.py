import random


while True:
    random_num = random.randrange(1, 4)
    options = {1: "rock", 2: "paper", 3: "scissors"}
    computer_choice = options[random_num]
    answer = input()
    if answer == "!exit":
        print("Bye!")
        break

    if answer == "scissors":
        if computer_choice == "rock":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "scissors":
            print(f"There is a draw ({computer_choice})")
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
    elif answer == "rock":
        if computer_choice == "paper":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "rock":
            print(f"There is a draw ({computer_choice})")
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
    elif answer == "paper":
        if computer_choice == "scissors":
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice == "paper":
            print(f"There is a draw ({computer_choice})")
        else:
            print(f"Well done. Computer chose {computer_choice} and failed")
    else:
        print("Invalid input")
