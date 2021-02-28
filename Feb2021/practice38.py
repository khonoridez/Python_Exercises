class Product:
    def __init__(self, product_name, product_cost, product_quantity, product_count):
        self.product_name  = product_name
        self.product_cost = float(product_cost)
        self.product_quantity = int(product_quantity)
        self.count = int(product_count)      
    def product_info(self):
        return 'Product {} Info \nProduct Name: {}\nProduct Cost: ${:.2f}\nProduct quantity on hand: {}\nTotal Product Cost: ${:.2f}'.format(self.count,self.product_name,self.product_cost,self.product_quantity,self.get_total_product_cost())
    def get_total_product_cost(self):        
        return self.product_cost * self.product_quantity
        
list_products = []
total_cost = 0

product_index = 2

for i in range (product_index):
    print('Product ' + str(i+1))
    product_name = str(input("Enter the product name: "))
    product_cost = float(input("Enter the product cost: "))
    product_quantity = int(input("Enter the quantity on hand: "))
    # appending instances to list
    list_products.append(Product(product_name, product_cost, product_quantity, i+1))
    print()

for product in list_products: 
    print(product.product_info())
    total_cost = total_cost + product.get_total_product_cost()
    print()

print("Total Cost: ")
print("${}".format(str(total_cost)))
