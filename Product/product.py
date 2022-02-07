from dataclasses import dataclass

@dataclass()
class Product:
    __price: float
    name: str
    discountPercent: float

    def getDiscountAmount(self):
        return self.__price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()
