user_weight = float(input('Enter Your Weight : '))
weight_unit = input('Kilograms or Pounds (K or L) : ')

if weight_unit == 'K':
    user_weight = user_weight * 2.205
    unit = 'Lbs.'
    print(f'your weight is : {round(user_weight, 1)} {unit}')    

elif weight_unit == 'L':
    user_weight = user_weight / 2.205
    unit = 'Kgs.'
    print(f'your weight is : {round(user_weight, 1)} {unit}')    
else:
    print('Please enter a valid unit')        
