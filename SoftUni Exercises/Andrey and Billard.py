number_of_products = int(input('Amount of products: '))
product_prices = {}
customers = {}
total_bill = 0.0

class Customer:

    def __init__(self, name):
        
        self.name = name

        self.orders = {}
        self.bill = 0

    def PrintOrders(self):
        print('\n\t' + self.name)
        # It's more accurate for the products to not be ordered... just flexing
        for prod, quant in sorted(self.orders.items(), key=lambda item: item[0]):
            print(f'-- {prod} - {quant}')
        print(f' Bill: {self.bill:.2f}')
    
    def AddOrder(self, product, quantity):
        if product not in self.orders:
            self.orders[product] = quantity
        else:
            self.orders[product] += quantity
        self.bill += product_prices[product] * int(quantity)
            
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
        customer_det = cmd.split()
        if customer_det[1] in product_prices.keys():            
            if customer_det[0] not in customers:                
                customers[customer_det[0]] = Customer(customer_det[0]) # Creating instances of Customer
            # If the customer already ordered - add his current order to the previous one
            customers[customer_det[0]].AddOrder(customer_det[1], customer_det[2])

# Output

for cust in sorted(customers):
    total_bill += customers[cust].bill
    customers[cust].PrintOrders()

print(f'\nTotal bill: {total_bill:.2f}')
