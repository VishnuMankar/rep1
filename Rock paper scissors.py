user_name = input('Please enter your name : ')

print(f'Hey {user_name} welcome to the game')

user_score = 0

computer_score = 0

import random

plays = ['rock' , 'paper' , 'scissors']

keep_playing = True

while keep_playing == True :

 c_plays = random.choice(plays)

 user_plays = input('what is your move: rock , paper or scissors : ')

 print(f'the computer chooses: {c_plays}')

 if c_plays == user_plays :

  print('tie')

  print(user_score)

  print(computer_score)

 elif c_plays == 'rock' and user_plays == 'paper' :

  print('you won')

  user_score +=1

  print(user_score)

  print(computer_score)

 elif c_plays == 'rock' and user_plays == 'scissors' :

  print ('you lose')

  computer_score += 1

  print(user_score)

  print(computer_score)

 elif c_plays == 'paper' and user_plays == 'scissors' :

  print('you win')

  user_score +=1

  print(user_score)

  print(computer_score)

 elif c_plays == 'paper' and user_plays == 'rock' :

  print('you lose')

  computer_score += 1

  print(user_score)

  print(computer_score)

 elif c_plays == 'scissors' and user_plays == 'rock':

  print('you win')

  user_score +=1

  print(user_score)

  print(computer_score)

 elif c_plays == 'scissors' and user_plays == 'paper':

  print('you lose')

  computer_score += 1

  print(user_score)

  print(computer_score)

 elif user_plays == 'quit' :

 	break else :

 	print('please enter a valid input')
