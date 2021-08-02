weight = input('What is your weight? ')
print(f'''Please kindly specify if your weight is in pounds or in kilos below.
input 'K' for Kilos and 'L' for Pounds''')
kilo = float(weight) * 0.453952
pounds = float(weight) / 0.453952
unit = input('(K)g or (L)bs? ')
kilogram = 'K'
lbs = 'L'
typed_unit = unit.upper()
if typed_unit == kilogram:
    print(f'Your converted weights in pounds is {pounds}lbs')
elif typed_unit == lbs:
    print(f'Your converted weights in kilo is {kilo}kg')
else:
    print(f'''You have inputted the wrong unit for your weights.
kindly, input 'K' for Kilos and 'L' for Pounds''')
