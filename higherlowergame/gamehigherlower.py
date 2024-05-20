from image import logo ,vs
print(logo)
from game_data import data
import random


def format_data(account):
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name} a {account_descr} from {account_country}"

def check_answer(guess,a_followers,b_followers):
    if  a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
    
score=0
account_b=random.choice(data)
#  for continue game 
continue_game=True
while continue_game:

# generate a random account from the game data
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"compare A :{format_data(account_a)}  .")
    print(vs)
    print(f" Against B :{format_data(account_b)} .")

    #  for guess
    guess=input("guess which have more follower 'A ','B'").lower()



    # get the follower count of each acc
    a_follower_account=account_a["follower_count"]
    b_follower_account=account_b["follower_count"]

    is_correct=check_answer(guess,a_follower_account,b_follower_account)


    if is_correct:
        score += 1
        print(f"you are right! current_score: {score}")
    else:
        continue_game=False
        print(f"you are wrong  ! sorry your score is {score}")



# clear the screen
