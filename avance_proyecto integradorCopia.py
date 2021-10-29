import random

def crear_filas_ecuaciones(n,variables,valores):  #función que crea y muestra las ecuaciones del sistema
    #n es entero y su range es entre 2 y 8
    
   # print(valores)
    for k in range(0,n):
        ecuacion = ""
        lista_coeficientes = [] #lista de coeficientes
        suma = 0
        
        for i in range (1,n+1):
            lista_coeficientes.append(random.randint(1,10))          #asignamos coeficientes al azar
            espositivo = random.randint(0,1)                         #asignamos una valor positivo o negativo al azar
            #print(espositivo)
            
            if espositivo == 0:                                              
                lista_coeficientes[i-1] = lista_coeficientes[i-1]*-1
                      
            if lista_coeficientes[i-1] >= 1 and i>1:               
                ecuacion = ecuacion+"+"+(str(lista_coeficientes[i-1])+variables[i])
            else:
                ecuacion = ecuacion+(str(lista_coeficientes[i-1])+variables[i])
            
            suma += lista_coeficientes[i-1]*valores[variables[i]]       #se suma el coeficiente multiplicado por el valor de la variable
            #print(suma)
            
        print(f"{ecuacion} = {suma}")
        #print(coeficiente)

def verificar_soluciones(valores,variables):   #función que pide y verifica la solución del usuario
    #print(soluciones)
    soluciones = {}                               #diccionario vacío en el que se guardaran las soluciones dadas
    for i in range(1, len(valores) + 1):
        respuesta = "" 
        while type(respuesta) == str:
            respuesta = input(f"El valor de la variable {variables[i]}: ")
           # print(respuesta[0])
            #print(respuesta[1])
            if respuesta.isnumeric() ==  True or (respuesta[0] == "-" and respuesta[1].isnumeric() == True):   #is alpha()
                    respuesta = int(respuesta)          
            else:   
                    respuesta = ""  
                    print("El valor de la variable debe ser un número entero")                  
            soluciones[variables[i]] = respuesta      #se pide que el usuario ingrese la solución y se agrega al diccionario
                                                                                                #la variables es el apendice, la solución el valor asignado a la variable
    if soluciones == valores:                                                                   #verificamos si el diccionario original con los valores es igual al nuevo creado
        print("Solución correcta")                                                              #si son iguales, dio la solución correcta
    else:
        print("Solución incorrecta, los valores correctos son: ")              #si no son iguales, despliega las soluciones
        for i in range(1, len(valores) + 1):
            print(f"{variables[i]} = {valores[variables[i]]}")

variables = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}  #diccionario de variables
valores = {}  #diccionario vacío con valor de cada variable  
n = "0"
while (int(n)<2 or int(n)>8):
   n = input("Ingrese el número de variables: ")  #pedimos la entrada n
   if n.isnumeric() == False:                      #se verifica si el string puesto es númerico
       n="0"                                       #si no lo es, asigna 0 a n, manda el mensaje y lo vuelve a pedir
       print("ERROR. La variable a ingresar debe ser un número entero entre 2 y 8")  
   elif (int(n)<2 or int(n)>8):                                            #n es númerico pero fuera de rango
       print("ERROR. La variable a ingresar debe ser un número entero entre 2 y 8")

n = int(n)    #convertimos a entero el valor de n aceptado
#print(n)

random.seed(10)
for i in range (1,n+1):                   #se crea el diccionario con los valores de cada variable
    valor = random.randint(-10,10)
    valores[variables[i]] = valor
    

crear_filas_ecuaciones(n,variables,valores) 
verificar_soluciones(valores,variables)



#crearFilaEc(2)
#crearFilaEc(3)

