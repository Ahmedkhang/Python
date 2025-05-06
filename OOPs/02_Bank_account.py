accounts = []
class Account:
    def __init__(self,name,account_no,password,initial_deposit):
        self.name = name
        self.account_no = account_no
        self.password = password
        self.initial_deposit = initial_deposit
        self.transactions = []
    def debit(self,amount):
        self.initial_deposit += amount
        print(f'{amount} deposited successfully')
        self.transactions.append(f'Deposited {amount} successfully')
    def withdrawal(self,amount):
        self.initial_deposit -= amount
        print(f'{amount} withdrawn successfully')
        if self.initial_deposit < 0:
            print('Insufficient balance')
            self.initial_deposit += amount
        else:
            print(f'{amount} withdrawn successfully')
        self.transactions.append(f'Withdrwawal {amount} successfully')
    def view_balance(self):
        print(f'Total Balance : {self.initial_deposit}')
    def view_transaction(self):
        for transactions in self.transactions:
            print(transactions)

def register():
    name = input('Enter your name: ')
    account_no = input('Enter your account number: ')
    password = input('Enter your password: ')
    initial_deposit = int(input('Enter your initial deposit: '))
    account = Account(name,account_no,password,initial_deposit)
    accounts.append(account)
    print('Account created successfully')   
def login():
    account_no = input('Enter your account number: ')
    password = input('Enter your password: ')
    for account in accounts:
        if account.account_no == account_no and account.password == password:
            print('Login successful')
            
            return account
    print('Invalid account number or password')
    return None                     

def user_menu(acc):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. View Transactions\n5. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = int(input("Enter deposit amount: "))
            acc.debit(amount)
        elif choice == '2':
            amount = int(input("Enter withdrawal amount: "))
            acc.withdrawal(amount)
        elif choice == '3':
            acc.view_balance()
        elif choice == '4':
            acc.view_transaction()
        elif choice == '5':
            print("Logged out.")
            break
        else:
            print("Invalid choice")
while True:
    print("\n--- Bank System ---")
    print("1. Register\n2. Login\nq. Quit")
    option = input("Choose an option: ")

    if option == '1':
        register()
    elif option == '2':
        user = login()
        if user:
         user_menu(user)
    
    elif option.lower() == 'q':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid input")
