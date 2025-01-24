class phone():
    chargertype="B-TYPE"
    def __init__(self,brand,price):
     self.brand=brand
     self.price=price
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("Chargertype:",self.chargertype)
samsung=phone("redmi","12555")
samsung.display()
realme=phone("realme","30000")
realme.display
