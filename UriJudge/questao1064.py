numeros = []
cont = 0
positivos =0



def calc():
    numeros = []
    cont = 0
    positivos =0
    numerosP = []
    while(cont<6):
        numeros.insert(cont, float(input()))
        if(numeros[cont]>0):
            numerosP.insert(cont,float(input()))
            positivos = positivos +1
    
        cont= cont+1
    if(positivos == 0):
        calc()    
    else:
        print(positivos, "valores positivos")
        media = sum(numeros) / len(numeros)
        print( "%.1f" %media)

calc()    





