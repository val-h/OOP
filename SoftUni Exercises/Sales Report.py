n = int(input('Number of elements: '))

salesByCity = {}

class Sales:

    def __init__(self, city, product, price, quantity):

        self.city = city
        self.product = product
        self.profit = float(price) * float(quantity)

# Reads a sale from the cmd and makes it an instance of Sales
def ReadSale():
    usrInp = input('Sale: ')
    saleArr = usrInp.split()
    sale = Sales(saleArr[0], saleArr[1], saleArr[2], saleArr[3])
    return sale

# Adding the sales to a ditionary
for i in range(0, n):
    sale = ReadSale()
    if sale.city not in salesByCity:
        salesByCity[sale.city] = sale.profit
    else:
        salesByCity[sale.city] += sale.profit

# Sorts the keys and values in salesByCity(since its a dict :/ ) and prints them
for key, value in sorted(salesByCity.items()):
    print(f'{key} -> {value}')
