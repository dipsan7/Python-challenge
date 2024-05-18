logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                 
print(logo)
import random
def deal_card():
    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

def comapre(user_score,computer_score):
     if user_score >computer_score:
          return"you won"
     elif user_score==computer_score:
          return "Draw"
     elif user_score==0:
          return "win with Blackjack"
     elif computer_score==0:
          return "win with Blackjack"
     elif user_score>21:
          return "opponent went over. You win"
     elif computer_score>21:
          return "opponent went over. You win"
     else:
          return "you lose"
def play_game(): 
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for _ in range(2):  
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards:{user_cards},current_score:{user_score}")
        print(f"first computer card:{computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score >21:
            is_game_over=True
        else: 
            user_should_deal=input(("type 'y' to get another card ,type 'n'to pass"))
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over =True

    while computer_cards !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"your final hand :{user_cards},final_score{user_score}")
    print(f"computer fina_score:{computer_cards},final:score{computer_score}")
    print(comapre(user_score,computer_score))
while input("do you want to a play a game of Black? type 'y' or 'n'")=='y':
    #  clear()
     play_game()



       
      

