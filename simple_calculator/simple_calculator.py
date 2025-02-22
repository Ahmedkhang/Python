user_guess = input('Enter an operator (+,-,*,/) = ')
num1 = float(input('Enter the first number : '))
num2 = float(input('Enter the second number : '))

if user_guess == '+':
    print(num1 + num2)
elif user_guess == '-':
     print(num1 - num2)
elif user_guess == '*':
      print(num1 * num2)
elif user_guess == '/':
      print(num1 / num2)  
else:
     print('Please enter the valid operator')                   