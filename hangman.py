# hangman
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game=False
word_list=["ram","sam","dam","kam","tan","word","dip","san","ran"]
word=random.choice(word_list)
print(word)
display=[]
word_len=len(word)
lives=6
for _ in range(word_len):
    display += "_"
# print(display)

while not end_of_game:
    guess=input("guess letter: ").lower()
    if guess in display:
        print(f"you already guess{guess}")
    for position in range(word_len):
        letter=word[position]
        if letter==guess:
            display[position]=letter
    if guess not in word:
        print(f"you guessed {guess},that is not in word so you lost live")
        lives -=1
        if lives==0:
            end_of_game=True
            print("you lose")


    print(display)
    if "_" not in display:
        end_of_game=true
        print("you won")
print(stages[lives])