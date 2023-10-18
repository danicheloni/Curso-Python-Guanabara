import random
import time

choices_list= ["rock", "paper", "scissors"]
print ("Choose rock, paper, or scissors")

def winner(user_choice, pc_choice):
    if user_choice == "scissors" and pc_choice == "paper":
        print("User wins")
    elif user_choice == "paper" and pc_choice == "rock":
        print("User wins")
    elif user_choice == "rock" and pc_choice == "scissors":
        print("User wins")
    else:
        print("PC wins")

def game(user_choice, pc_choice):
    if user_choice == pc_choice:
        print("It's a draw! Lets try again!")
    else:
         winner(user_choice, pc_choice)

#________________________________________________

user_choice = input("Wich one do you choose? ")

pc_choice = random.choice(choices_list)

print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!!')
time.sleep(1)

print("The computer choose: ", pc_choice)

game(user_choice, pc_choice)