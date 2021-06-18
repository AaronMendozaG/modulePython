class Producto(object):
    def __init__(self,price):
        self.price=price
        self.priceIva=0
        self.impuesto=0
        self.subTotal=0
        self.total=0
        self.car=0
    def changePrice(self,newPrice):
        self.price=newPrice
        print("Precio modificado")
    def addToCar(self,cantidad):
        self.car+=cantidad
        print(f"Se agrego la cantidad al carrito, cantidad actual {self.car}")
    def priceIvaF(self):
        self.priceIva = self.price*.16 + self.price
        print(f"El precio con IVA es {str(self.priceIva)}")
    def infoCar(self):
        self.impuesto=self.car*self.price*.16
        self.subTotal=self.price*self.car
        self.total=self.subTotal+self.impuesto
        print(f"El Impuesto es de {self.impuesto}")
        print(f"El Subtotal es de {self.subTotal}")
        print(f"El Total es de {self.total}")



agua=Producto(15)
agua.price
agua.changePrice(1)
agua.addToCar(5)
agua.car
agua.priceIvaF()
agua.infoCar()