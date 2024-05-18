logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)

from random import randint
Easy_level_turn=10
Hard_level_turn=5
turns=0
def check_answer(guess,answer,turns):
    """Checks answer against guess"""
    if guess>answer:
        print("Too high. ")
        return turns -1
    elif guess<answer:
        print("too low .")
        return turns -1
    else:
        print(f"you got it .The answer is {answer}.")

# make function to set difficult
def set_difficult():
    level=input("chooose the difficulty level hard for 'hard' and 'easy' for easy")
    if level=="easy":
        global turns
        return Easy_level_turn
    else:
        return Hard_level_turn
    
def game():
# choosing a random number between 1 and 100
    print("Welcome to Number Guessing Game")
    print("i'm thinking of number between 1 and 100")
    answer=randint(1,100)
    print(f" the correct answer is {answer}")

    turns=set_difficult()
    
    # let the user guess number
    guess=0
    while guess !=answer:
      print(f"you have{turns} attempts remaining to guess the number")
      guess=int(input("enter your guess number"))
      turns=check_answer(guess,answer,turns)
      if turns==0:
          print("Yoou've runout of attempy you lose")
          return 
    #   elif guess !=answer:
    #       print(f"")

game()

