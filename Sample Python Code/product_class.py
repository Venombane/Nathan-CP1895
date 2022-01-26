class Product:
    def __init__(self, name: str, price: float, discount_percent: int):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def getDiscountAmount(self):
        return round(self.price * (self.discount_percent / 100), 2)

    def getDiscountPrice(self):
        return round(self.price - self.getDiscountAmount(), 2)


product1 = Product('Stanley 13 Ounce Wood Hammer', 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0)

print(f"Name:               {product1.name}")
print(f"Price:              {product1.price}")
print(f"Discount Percent:   {product1.discount_percent}%")
print(f"Discount Amount:    {product1.getDiscountAmount()}")
print(f"Discount Price:     {product1.getDiscountPrice()}")
print("------------------------------------------------------|")
print(f"Name:               {product2.name}")
print(f"Price:              {product2.price}")
print(f"Discount Percent:   {product2.discount_percent}%")
print(f"Discount Amount:    {product2.getDiscountAmount()}")
print(f"Discount Price:     {product2.getDiscountPrice()}")
