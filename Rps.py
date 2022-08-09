import random

print( 'Rock, Paper, Scissors Game')
option = input('Choose one:').lower()
# print(option)

randomNumber = int(random.random() * 3)

rockPaperScissors = ['rock', 'paper', 'scissors']
computerOption = rockPaperScissors[randomNumber]

result = f'You chose {option} and computer chose {computerOption}'

# print(rockPaperScissors[randomNumber])

if option != 'rock' and option != 'paper' and option != 'scissors':
    print(f"You didn't pick a valid option")
elif option == 'rock' and computerOption == 'scissors':
    print(result)
    print(f'You win because {option} wins {computerOption}')
elif option == 'paper' and computerOption == 'rock':
    print(result)
    print(f'You win because {option} wins {computerOption}')
elif option == 'scissors' and computerOption == 'paper':
    print(result)
    print(f'You win because {option} wins {computerOption}')
elif option ==  computerOption:
    print(result)
    print(f"it's a tie")
else:
    print(result)
    print(f'You lose because {computerOption} wins {option}')




