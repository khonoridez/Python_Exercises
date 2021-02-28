class Product:
    def __init__(self):
        self.product_name  = "none"
        self.product_cost = float(0.00)
        self.product_quantity = int(0)
    def product_info(self):
        return 'Product Name: {}\nProduct Cost: ${:.2f}\nProduct quantity on hand: {}\nTotal Product Cost: ${:.2f}'.format(self.product_name,self.product_cost,self.product_quantity,self.get_total_product_cost())
    def get_total_product_cost(self):        
        return self.product_cost * self.product_quantity
        
list_products = []
total_cost = 0
counter = 0

product_index = 2

for i in range (product_index):
    print('Product ' + str(i+1))
    product = Product()
    product.product_name = str(input("Enter the product name: "))
    product.product_cost = float(input("Enter the product cost: "))
    product.product_quantity = int(input("Enter the quantity on hand: "))
    # appending instances to list
    list_products.append(product)
    print()

for product in list_products:
    counter = counter + 1
    print('Product ' + str(counter) + ' Info')
    print(product.product_info())
    total_cost = total_cost + product.get_total_product_cost()
    print()

print("Total Cost: ")
print("${0:.2f}".format(total_cost))
