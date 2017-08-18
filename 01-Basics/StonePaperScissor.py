import random

a = ["stone","paper","scissor"]
cpu_choice = random.choice(a)
gameLoop = True

while gameLoop:

    user_choice = input("Enter your choice : ")

    print("CPU's choice",cpu_choice)

    if user_choice == cpu_choice:
        print("Match Tie")
    elif user_choice == "paper" and cpu_choice == "stone":
        print("You win")
    elif user_choice == "scissor" and cpu_choice == "paper":
        print("You win")
    elif user_choice == "stone" and cpu_choice == "scissor":
        print("You win")

    elif user_choice == "stone" and cpu_choice == "paper":
        print("CPU win")
    elif user_choice == "paper" and cpu_choice == "scissor":
        print("CPU win")
    elif user_choice == "scissor" and cpu_choice == "stone":
        print("CPU win")

    else:
        print("Wrong Choice")

    cpu_choice = random.choice(a)