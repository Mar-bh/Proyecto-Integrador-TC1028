import random

def crearFilaEc(n): #n es entero y su range es entre 2 y 8

    variables = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
    valores = {}  #valor de cada variable
    coeficiente = [] #lista de coeficientes
    ecuacion = ""
    
    for i in range (1,n+1):
        valor = random.randint(-10,10)
        valores[variables[i]] = valor
    
    #print(valores)
    for k in range(0,n):
        ecuacion = ""
        coeficiente = []
        for i in range (1,n+1):
            coeficiente.append(random.randint(1,10))
            espositivo = random.randint(0,1)
            #print(espositivo)
        
            if espositivo == 0:
                coeficiente[i-1] = coeficiente[i-1]*-1
            
            if coeficiente[i-1] >= 1 and i>1:
                ecuacion = ecuacion+"+"+(str(coeficiente[i-1])+variables[i])
            else:
                ecuacion = ecuacion+(str(coeficiente[i-1])+variables[i])
            
        print(ecuacion)
        #print(coeficiente)


crearFilaEc(2)
#crearFilaEc(3)
#crearFilaEc(4)