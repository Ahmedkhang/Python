import random
def main():
    balance = 100
    print('-------- Welcome to Slot Machine --------')
    print('------ Symbols : 🍉🍒🍋🔔⭐')
    print('-----------------------------------------')
    while balance > 0:
        print(f'Current Balance : ${balance}')
        bet = input('Enter the bet : ')
        if not bet.isdigit():
            print(f'{bet} is not a valid number')
            continue
        bet = int(bet)
        if bet > balance:
             print('Insufficient balance')
             continue
        if bet <= 0:
            print('bet should be greater than 0')
            continue
        balance -= bet
        row = spin_row()
        print(row)
        payout = getPayout(row, bet)
        print(f'you won : ${payout}')
        balance += payout
        play_again = input('do you want to play again? (y/n) : ')
        if play_again == 'n':
            break

def print_row(row):
    print('------------------')


def spin_row():
    symbols = ['🍉','🍒','🍋','🔔','⭐']
    return [random.choice(symbols) for _ in range(3)]
   
def getPayout(row, bet):
    if row[0] == row[1] == row[2]:
        if row == '🍉':
           return bet * 2
        elif row == '🍒':
           return bet * 3
        elif row == '🍋':
           return bet * 4
        elif row == '🔔':
           return bet * 5
        elif row == '⭐':
           return bet * 10     
    return 0                  


if __name__ == '__main__':
     main()