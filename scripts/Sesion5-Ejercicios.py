## actualizar el siguiente diccionario dict_ejercicio
l_nombres2 = ['Aaron','Antonio','Ferdi']
l_horas = [6,8,7]
 
dict_ejercicio = {}
dict_ejercicio.clear() 
for i, j in zip(l_nombres2, l_horas):
    #dict_ejercicio.update({i: j})
    dict_ejercicio.setdefault(i, j)
   # dict_ejercicio[i] = j
    print(f'{i} duerme {j} horas')


##PEDIR AL USER NOMBRE Y TIEMPO

nuevo_dict={}

while True:
    nombre=input("Inserta el nombre del alumno: ")
    minutos=int(input("Ingrese un numero en minutos: "))
    if nombre == 'NO':
        break
    nuevo_dict.update({nombre:minutos})

    if nombre in nuevo_dict.keys():
        

for nombre,minutos in nuevo_dict.items():
