import random

print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')


choices = ['Rock', 'Paper','Scissors', 'Lizard', 'Spock']

# print('1) ✊ Rock')
# print('2) ✋ Paper')
# print('3) ✌️ Scissors')
# print('4) 🦎 Lizard')
# print('5) 🖖 Spock')

player = (input('Choose: \n Rock \n Paper \n Scissors \n Lizard \n Spock \n '))

computer = choices[random.randint(0, 4)]

# Map numbers to choices
# if computer == 1:
#     computer = 'Rock'
# elif computer == 2:
#     computer = 'Paper'
# elif computer == 3:
#     computer = 'Scissors'
# elif computer == 4:
#     computer = 'Lizard'
# else:
#     computer = 'Spock'

print(f"You Chose: {player}")
print(f'Computer Chose: {computer}')

# Determin the Winner
if player == computer:
    print("It's a Tie")
elif (player == 'Scissors' and computer == 'Paper') or \
     (player == 'Paper' and computer == 'Rock') or \
     (player == 'Rock' and computer == 'Lizard') or \
     (player == 'Lizard' and computer == 'Spock') or \
     (player == 'Spock' and computer == 'Scissors') or \
     (player == 'Scissors' and computer == 'Lizard') or \
     (player == 'Lizard' and computer == 'Paper') or \
     (player == 'Paper' and computer == 'Spock') or \
     (player == 'Spock' and computer == 'Rock') or \
     (player == 'Rock' and computer == 'Scissors'):
    print('You Win!')
else:
    print('You Lose')