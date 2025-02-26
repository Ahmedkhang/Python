 # temperature Conversion

# step 1 getting input from user in a variables
temp_unit = input('Enter the temperature unit (C or F) : ')
user_temp = float(input('Enter the temperature : '))

# checking if the given temp unit will be C

if temp_unit == "C":
    temp = (9 * user_temp) / 5 + 32
    print(f'The temperature is : {temp}')
# checking if the given temp unit will be F
elif temp_unit == "F":
    temp = (user_temp - 32) * 5 / 9 
    print(f'The temperature is : {temp}')
else:
    print(f'{temp_unit} is not a valid unit')    
