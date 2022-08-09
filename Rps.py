from ast import While
import random

while True:
    rockPaperScissors = ['rock', 'paper', 'scissors']
    randomNumber = int(random.random() * 3)
    computerOption = rockPaperScissors[randomNumber]
    print( 'Rock, Paper, Scissors Game')
    option = ''

    while option not in rockPaperScissors:
        option = input('Choose one:').lower()

    result = f'You chose {option} and computer chose {computerOption}'

    if option == 'rock' and computerOption == 'scissors':
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
        
    playAgain = input("Play again? (y/n):").lower()

    if playAgain != 'y':
        break

print('Bye!!')



