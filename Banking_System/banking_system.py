
# declaring Functions

def show_balance():
    print(f'Your Balance is : ${balance:.2f}')

def deposit():

  amount = float(input('Enter an amount to be deposited : '))
  if amount < 0:
            print('Please enter a valid amount')

  else:
   return amount


def withdraw():
    amount = float(input(f'Enter amount to be withdrawn : '))

    if amount > balance:
        print('Please Enter a valid amount')
    else:
        return amount    

#    declaring Globle Variiable

balance = 0
isRunning = True

# Loop for Banking System

while isRunning:
    print('Banking Program')
    print('1. Show Balance')
    print('2. depost')
    print('3. withdraw')
    print('4. Exit' )

  # getting User Input
    user_input = input('Choose between 1-4: ')
    if user_input == '1':
        show_balance()
    elif user_input == '2':
       balance += deposit()
    elif user_input == '3':
      balance -=  withdraw()
    elif user_input == '4':
        isRunning = False
    else:
        print('please choose between 1-4')  
