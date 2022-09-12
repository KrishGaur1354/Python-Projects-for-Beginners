import random

def play():
    print("Wlcome to Rock | Paper | Scissors")
    print("r is Rock")
    print("p is Paper")
    print("s is Scissors")
    user = input("Enter your choice:\n")
    game = random.choice(['r', 'p', 's'])

    if user == game:
        return 'The Game is Tied'

    if is_win( user, game):
        return 'You won!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
