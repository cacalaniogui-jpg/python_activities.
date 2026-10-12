import random
choices=["rock","paper","scissor"]

while True:
    print("----Rock Paper Scissor Game----")
    print("Choices: ", choices)
    user_choice = input("Enter a choice(write quit to exit)").lower()

    if user_choice == "quit":
        print("Game Over")
        break
    if user_choice not in choices:
        print("Invalid choice,write another!")
        continue

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print(f"user{user_choice} vs. computer{computer_choice} = Its a Tie")
        continue
    elif(user_choice == "rock" and computer_choice == "scissor" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissor" and computer_choice == "paper"):

         print(f"user{user_choice} vs. computer{computer_choice} = You Win") 

        print(f"user{user_choice} vs. computer{computer_choice} = You Win") 
        continue
    elif(user_choice == "scissor" and computer_choice == "rock" or user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissor"):
        
        print(f"user{user_choice} vs. computer{computer_choice} = Computer Win") 
        continue

    