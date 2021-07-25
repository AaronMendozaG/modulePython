## Ejemplo de función para conocer importancia de tuplas
def prueba(i = []):
    i.append(1)
    print(i)
# Sintaxis de Clases
class Clase(object):
    pass
# Métodos
class Celular(object):
    def llamar(self):
        print("Iniciando llamada")
    def colgar(self):
        print("Se termino la llamada")
mi_cel = Celular()
mi_cel.llamar()
mi_cel.colgar()
# Atributos
class Celular(object):
    estado = "en llamada"
    marca = "Nokia"
    def llamar(self):
        self.estado = "en llamada"
        print("Iniciando llamada")
    def colgar(self):
        self.estado = "en modo ahorro de energia"
        print("Se termino la llamada")
### Crear una clase de tu comida favorita
mi_cel = Celular()
mi_cel.estado
mi_cel2 = Celular()

class Comida(object):
    rebanadas="6 rebanadas"
    sabor="Hawaiana"

    def comer(self):
        self.rebanadas="3 rebanas"
        print("Se comieron parte de la pizza")
    def agregarIng(self):
        self.sabor="Hawaina mas Salsa"
        print("Se agrego salsa a la pizza")

pizza=Comida()
pizza.sabor
pizza.rebanadas
pizza.comer()
pizza.agregarIng()






# Constructor
class Celular(object):
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
    def llamar(self):
        self.estado = "en llamada"
        print("Iniciando llamada")
    def colgar(self):
        self.estado = "en modo ahorro de energia"
        print("Se termino la llamada")
mi_cel = Celular("Xiaomi", "en modo ahorro de energia")
mi_cel2 = Celular("Nokia", "en llamada")
# usar self.i como contador
class Acumulador(object):
    def __init__(self):
        self.acum=0
    def sumar_una_unidad(self):
        self.acum+=1
    def resta_una_unidad(self):
        self.acum-=1
    def mostar_acumulador(self):
        print(self.acum)   

test=Acumulador()
test.sumar_una_unidad()
test.mostar_acumulador()





#Ejercicio guiado volver nuestro código de registro de usarios visto en clase a la forma orientada a objetos
# Ejercicio en clase crea el objeto producto, 
# a partir de diferentes metodos crea las siguientes acciones:
# Definir un precio sin iva inicial del producto (Constructor) ok
# Modificar el precio actual del producto ok
# Comprar el MISMO producto y agregar al carrito ok
# Mostrar precio con iva del producto ok
# Mostrar el impuesto, subtotal y total de la cantidad de productos agregados al carrito

# class Producto(object):
#     def __init__(self,price):
#         self.price=price
#         self.priceIva=0
#         self.impuesto=0
#         self.subTotal=0
#         self.total=0
#         self.car=0
#     def changePrice(self,newPrice):
#         self.price=newPrice
#         print("Precio modificado")
#     def addToCar(self):
#         self.car+=1
#     def priceIvaF(self):
#         self.priceIva = self.price*.16 + self.price
#         print(f"El precio con IVA es {str(self.priceIva)}")
#     def infoCar(self):
#         self.impuesto=self.car*self.price*.16
#         self.subTotal=self.price*self.car
#         self.total=self.subTotal+self.impuesto
#         print(f"El Impuesto es de {self.impuesto}")
#         print(f"El Subtotal es de {self.subTotal}")
#         print(f"El Total es de {self.total}")


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


x=1
y=2
z=3
n=3
iterableList=[x,y,z]
# print(iterableList)
# if x>y and x>z :
#     newList=[[a,b,c] for a in iterableList for b in iterableList for c in iterableList ]
#     print(newList)
# elif y>x and y>z :
#     newList=[[a,b,c] for a in range(y+1) for b in range(y+1) for c in range(y+1) if (a+b+c) != n]
#     print(newList)
# elif z>x and z>y :
#     newList=[[a,b,c] for a in range(z+1) for b in range(z+1) for c in range(z+1) if (a+b+c) != n]
#     print(newList)
# elif x==y or x==z:
#     newList=[[a,b,c] for a in range(x+1) for b in range(x+1) for c in range(x+1) if (a+b+c) != n]
#     print(newList)
# elif y==z:
#     newList=[[a,b,c] for a in range(y+1) for b in range(y+1) for c in range(y+1) if (a+b+c) != n]
#     print(newList)
# elif z==x:
#     newList=[[a,b,c] for a in range(z+1) for b in range(z+1) for c in range(z+1) if (a+b+c) != n]
#     print(newList)

print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (a+b+c) != n])

if __name__ == '__main__':
    n = 5
    a=[2,3,3,6,5]
    arr = map(int, a.split())
aUno=a[::-1]
aUno
for i in a:
    for j in aUno:
        if i==j:
            print(i)
