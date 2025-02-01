toppings =['chocolate', 'vanilla', 'strawberry']
for topping in toppings:
    if topping == 'vanilla':
        print(topping)
        breakpoint

while True:
    password = input ('please input password here:')
    if password == 'scitt':
        print('access granted')
        breakpoint
    else:
        print('please enter  the correct password')     