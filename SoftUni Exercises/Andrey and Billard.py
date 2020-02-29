number_of_products = int(input('Amount of products: '))
product_prices = {}
customers = []
total_bill = 0.0

class Customer:

    bill = 0.0

    def __init__(self, name, product, quantity):
        
        self.orders = {}

        self.name = name
        self.product = product
        self.quantity = int(quantity)
        if product not in self.orders: self.orders[product] = quantity
        else: self.orders[product] += quantity        
        self.bill += self.quantity * product_prices[self.product]

    def PrintOrders(self):
        print(self.name)
        for prod, quant in sorted(self.orders.items(), key=lambda item: item[0]):
            print(f'-- {prod} - {quant}')
        print(f'Bill: {self.bill}')

# Receiving and storing the products
for i in range(0, number_of_products):
    user_inp = input(f'Product N{i+1}: ')
    product = user_inp.split('-')
    product_prices[product[0]] = float(product[1])

# Recieving customer orders until 'end of clients' command is given
while True:
    cmd = input('/> ')
    if cmd == 'end of clients': break
    else:   # Creating a list of information from the cmd
        cmd = cmd.replace('-', ' ').replace(',', ' ')
        customer_order = cmd.split()
        if customer_order[1] in product_prices.keys():  # Creating instances of Customer
            customers.append(Customer(customer_order[0], customer_order[1], customer_order[2]))

# Output
for cust in sorted(customers, key=lambda x: x.name):
    total_bill += cust.bill
    print(cust.PrintOrders())   # i dont know from where the 'None' comes from
print(f'Total bill: {total_bill}')
