#EJERCICIO 1
suma = lambda x,y: str(x)+str(y) if isinstance(x,str) or isinstance(y,str) else x+y
suma('9',0)

#EJERCIIO2 
dictionarie={
    'Clima':'calor'
}
lambDic=lambda dict: f"La llaves es {dict.keys()} y contiene {dict.values()}"
lambDic(dictionarie)

cel={
    'Modelo':'iPhone',
    'Almacenamiento':64,
    'Pantalla':'HDR'
}

cel['Almacenamiento']=cel['Almacenamiento']+10
cel  
            



