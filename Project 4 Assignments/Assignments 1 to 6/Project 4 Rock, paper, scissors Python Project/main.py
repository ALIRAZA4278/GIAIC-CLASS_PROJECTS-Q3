import random

def play():
    user = input("whats your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'Its is tie'
    
    if is_win(user, computer):
        return 'You win!'
    
    # if is_win(computer, user):
    #     return 'You lose!'
    
    return "you lost!"
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

print(play())