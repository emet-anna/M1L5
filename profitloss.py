#Write to check if a person is buying an orange at 10 kes and later selling it at 30 kes. Find if he has profit or loss?
actual_cost=float(input('Please enter the actual cost of product: '))
selling_price=float(input('Please enter the selling price of product: '))
if(selling_price>actual_cost):
    profit=selling_price-actual_cost
    print('Total profit={0}'.format(profit))
else:
    print('No profit!')