name = input('What is your name? ')
if (len(name)) > 50:
    print(f'Characters cannot be more than 50')
elif (len(name)) < 3:
    print(f'Character cannot be less than 3')
else:
    print(f'Name looks good!!!')
