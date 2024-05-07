# 0 for rock 1for  paper 2 for scissors
import random
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

'''
game_image=[rock,paper,scissors]  

user_choice=int(input("rock for 0 paper 1 and scissors for 2\n"))
print(game_image[user_choice])
computer_choice=random.randint(0,2)
print(game_image[computer_choice])
# print(f'computer choose{computer_choice}')
if user_choice == 0 and computer_choice == 2:  
    print("You win! 🎉")  
elif computer_choice == 0 and user_choice == 2:  
    print("You lose.  ☠")  
elif computer_choice > user_choice:  
    print("You lose. ☠")  
elif user_choice > computer_choice:  
    print("You win!🎉 ")  
elif computer_choice == user_choice:  
    print("It's a draw.")  
elif user_choice >= 3 or user_choice < 0:  
    print("You typed an invalid number, You Lose.  ☠")  