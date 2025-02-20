
menu = {
    'pizza':140,
    'bbq':120,
    'biryani':150,
    'nihari':250,
    'chai':50,
    'coke':80,
    'pepsi':80,
    'icecream':130,


}

# print welcome message to user & menu

print('Welcome to Arsii restaurant')
print('pizza:Rs140\nbbq:Rs120\nbiryani:Rs150\nnihari:Rs250\nchai:Rs50\ncoke:Rs80\npepsi:Rs80\nicecream:Rs130')

#
order_total = 0

# taking first order from user


choice = input('Enter a menu item to order = ')
#  checking if order is available

if choice in menu:
    order_total += menu[choice]
    print(f'Your item {choice} has been added')
else:
    print(f'This item {choice} is not available') 

# asking from user if he need something else

another_order = input('Do you want to order another item : (y/n)')
if another_order == 'y':
        another_item = input('Enter a menu item to order = ')
        #  checking if order is available
        if another_item in menu:
           print(f'Your item {another_item} has been added')
           order_total += menu[another_item]
else:
         print(f'This item {another_order} is not available')   
           
# printing total bill

print(f'Your total bill is : Rs{order_total} ')