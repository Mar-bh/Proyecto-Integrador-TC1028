import random

def crear_filas_ecuaciones(n,variables,valores): #n es entero y su range es entre 2 y 8
    
   # print(valores)
    for k in range(0,n):
        ecuacion = ""
        lista_coeficientes = [] #lista de coeficientes
        suma = 0
        
        for i in range (1,n+1):
            lista_coeficientes.append(random.randint(1,10))
            espositivo = random.randint(0,1)
            #print(espositivo)
            
            if espositivo == 0:
                lista_coeficientes[i-1] = lista_coeficientes[i-1]*-1
                      
            if lista_coeficientes[i-1] >= 1 and i>1:
                ecuacion = ecuacion+"+"+(str(lista_coeficientes[i-1])+variables[i])
            else:
                ecuacion = ecuacion+(str(lista_coeficientes[i-1])+variables[i])
            
            suma += lista_coeficientes[i-1]*valores[variables[i]]
            #print(suma)
            
        print(f"{ecuacion} = {suma}")
        #print(coeficiente)

def verificar_soluciones(valores,variables):
    #print(soluciones)
    soluciones = {}
    for i in range(1, len(valores) + 1):
        soluciones[variables[i]] = int(input(f"El valor de la variable {variables[i]}: "))
    
    if soluciones == valores:
        print("Solución correcta") 
    else:
        print("Solución incorrecta, los valores correctos son: ") 
        for i in range(1, len(valores) + 1):
            print(f"{variables[i]} = {valores[variables[i]]}")

variables = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
valores = {}  #valor de cada variable
n = 0
while (n<2 or n>8):
   n = int(input("Ingrese el número de variables: "))

for i in range (1,n+1):
    valor = random.randint(-10,10)
    valores[variables[i]] = valor
    

crear_filas_ecuaciones(n,variables,valores) 
verificar_soluciones(valores,variables)



#crearFilaEc(2)
#crearFilaEc(3)

