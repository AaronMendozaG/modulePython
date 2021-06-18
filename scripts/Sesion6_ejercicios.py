def sumTotal(*x):
    suma=0
    for i in x:
        suma=suma+i
    return suma

sumTotal(1,2,3,4)

def recursiva(n):
    if n==1:
        return(n)
    else:
        return (recursiva(n-1)*n)

def recursivaSum(n):
    if n==0:
        return(n)
    else:
        return(recursiva(n)+(n))

recursiva(6)
recursivaSum(3)

