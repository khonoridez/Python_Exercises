class Product:
    total_cost = 0
    def __init__(self):
        self.product_name  = "none"
        self.product_cost = float(0.0)
        self.product_quantity = int(0)
        self.count = int(0)      
    def product_info(self):
        return 'Product {} Info \nProduct Name: {}\nProduct Cost: ${:.2f}\nProduct quantity on hand: {}\nTotal Product Cost: ${:.2f}'.format(self.count,self.product_name,self.product_cost,self.product_quantity,self.get_total_product_cost())
    def get_total_product_cost(self):        
        return self.product_cost * self.product_quantity
        
    

list_count = []
list_product_names = []
list_product_costs = []
list_product_quantity= []

product = 2

for i in range (product):
    print('Product ' + str(i+1))
    i=i+1
    list_count.append(i)
    product_name = str(input("Enter the product name: "))
    list_product_names.append(product_name)
    product_cost = float(input("Enter the product cost: "))
    list_product_costs.append(product_cost)
    product_quantity = int(input("Enter the quantity on hand: "))
    list_product_quantity.append(product_quantity)
    print()

product_1 = Product()
product_1.product_name = list_product_names[0]
product_1.product_cost = list_product_costs[0]
product_1.product_quantity = list_product_quantity[0]
product_1.count = list_count[0]
product_2 = Product()
product_2.product_name = list_product_names[1]
product_2.product_cost = list_product_costs[1]
product_2.product_quantity = list_product_quantity[1]
product_2.count = list_count[1]

print(product_1 .product_info())
print()
print(product_2 .product_info())
print()
total_cost = ((product_1.get_total_product_cost())+(product_2.get_total_product_cost()))
print("Total Cost: ")
print("${}".format(str(total_cost)))




