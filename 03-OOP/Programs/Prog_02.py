# Create a class laptop with attributes: Brand , RAM , Price. Create two objects with different values.

class laptop:
    brand = "Default"
    ram = "8 GB"
    price = "60K"

laptop1 = laptop()
laptop1.brand = "Asus"
laptop1.price = "50K"

print(laptop1.brand)
print(laptop1.ram)
print(laptop1.price)

laptop2 = laptop()
laptop2.brand = "Mac"
laptop2.price = "70K"

print(laptop2.brand)
print(laptop2.ram)
print(laptop2.price)
