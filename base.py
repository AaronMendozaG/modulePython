#LISTAS
#ESTRUCUTRA DE DATOS EN PYTHON QUE NOS PERMITE ALAMACENAR CUALQUIER TIPO DE VALOR COMO 
#̦ENTEROS,CADENAS,FUNCIONES HASTA OTRAS LISTAS

##F-STRINGS

nombre="DyNet"
objetivo="Apoyamos en la proteccion de la infraestructura informatica"
queHace="Proteccion de seguridad perimetral, seguridad de datos y conectividad"

print(f'''Nombre: {nombre}
Objetivo: {objetivo}
Que hace?: {queHace}
''')


lista=[10,1,2,3,4]
list(map(lambda lista: str(lista),lista))
list(map(lambda lista: type(lista),lista))


