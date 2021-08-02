price_of_the_house = 1000000
ten_percent_of_price = (float(0.1) * price_of_the_house)
twenty_percent_of_price = (float(0.2) * price_of_the_house)
good_credit = False
if good_credit:
    print(f'Buyer need to put down ${ten_percent_of_price}')
else:
    print(f'Buyer needs to put down ${twenty_percent_of_price}')
print(f'Please kindly proceed to make payments')
print(f'Thanks for choosing us')
