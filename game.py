import random
#from unittest import result

print("List of the game: \n 1) Stone \n 2) Paper \n 3) Sissor")

while True:
    user_choice = int(input("Enter the choosed number: "))
    choice = ""

    if user_choice == 1:
        choice = "stone"
    elif user_choice == 2:
        choice = "paper"
    else:
        choice = "sissor"

    print("The Entered part is: ", choice)

    while True:
        
        # Now computer will choose
        comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            cmp_choice = "Stone"
        elif comp_choice == 2:
            cmp_choice = "paper"
        else:
            cmp_choice = "sissor"

        print("Computer choice: ", cmp_choice)

        #Now main one to let machine think
        if choice == cmp_choice:
            print("It's draw!")

        result = ""
        if (user_choice == comp_choice):
            print("Its draw!/tie")
        elif (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
            print("Paper Wins")
            #result = "paper"
        elif (user_choice == 1 and comp_choice == 3)or (user_choice == 3 and comp_choice == 1):
            print("Stone Wins!")
            #result = "stone"
        else:
            print("Scissor wins!")
            #result = "scissor"
        break 

    if result == choice:
        print("User Wins!")
    elif result == cmp_choice:
        print("Computer Wins!")
    break

print("Thanks for participating")
