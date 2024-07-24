import random
rounds=int(input("Enter the number of rounds: "))
user_points=0
comp_points=0
for i in range(0,rounds):
    user_choice=int(input("Enter your choice :type 0 for rock, 1 for paper and 2 for scissors: "))
    computer_choice=random.randint(0,2)
    print ("Computer choice: ")
    print(computer_choice)
    if user_choice<3 and computer_choice>=0:
        if computer_choice==user_choice:
            print("It's a draw")
        elif computer_choice==0 and user_choice==2:
            comp_points+=1 
            print("You loose")
        elif computer_choice==2 and user_choice==0:
            user_points+=1
            print("You win")
        elif computer_choice>user_choice:
            comp_points+=1
            print("You loose")
        elif user_choice>computer_choice:
            user_points+=1
            print("You win")
    else:
        print("You have entered a wrong choice, Please enter a no between 0,1 and 2")
print("Considering best of",rounds,":")
if user_points==comp_points:
    print("It's a draw")
elif user_points>comp_points:
    print("You win")
else:
    print("You loose")
