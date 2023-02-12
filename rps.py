import random

options = ['rock', 'paper', 'scissors']
counter_player = 0 
counter_computer = 0

max_score = int(input("Set max score: "))

def check(p, c):
    global counter_player, counter_computer
    
    if p == 'rock' and c == 'scissors':
        counter_player += 1
    elif p == 'rock' and c == 'paper':
        counter_computer += 1
    elif p == 'paper' and c == 'rock':
        counter_player += 1
    elif p == 'paper' and c == 'scissors':
        counter_computer += 1
    elif p == 'scissors' and c == 'paper':
        counter_player += 1
    elif p == 'scissors' and c == 'rock':
        counter_computer += 1
    else:
        pass
    return c

while True:
    player = None
    while player not in options:
        player = input("Choice one of rock, paper, scissors: ")

    computer=random.choice(options)
    check(p=player, c=computer)
    print(f"Player: {player} Computer: {computer}")
    print(f"Score: Player {counter_player} - {counter_computer} Computer")

    if counter_computer == max_score:
        print(f"Computer wins {counter_computer} to {counter_player}!")
        break
    elif counter_player == max_score:
        print(f"Player wins {counter_player} to {counter_computer}!")
        break
