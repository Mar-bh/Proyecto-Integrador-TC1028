#Integrantes: Mariana Bustos Hernández-A01641324, Paulina Reyes Ramírez-A01641231, Veronica Jeannine Tinajero Guzman - A01641911

import random

def main():

    eleccion_modo = input("\U0001F914 Para elegir el modo normal ingresa 1, para elegir modo aventura ingresa cualquier otro valor alfanúmerico: ")
    if eleccion_modo == "1":
        modo_normal() #Llamada al modo normal
    else:
        modo_aventura()  #LLamada al modo aventura

def crear_filas_ecuaciones(n,variables,valores):  #función que crea y muestra las ecuaciones del sistema

    for k in range(0,n):
        ecuacion = ""
        lista_coeficientes = [] 
        suma = 0

        for i in range (1,n+1):
            lista_coeficientes.append(random.randint(1,10))          #asignamos coeficientes al azar
            espositivo = random.randint(0,1)                         #asignamos una valor positivo o negativo al azar
            if espositivo == 0:                                              
                lista_coeficientes[i-1] = lista_coeficientes[i-1]*-1  
            if lista_coeficientes[i-1] >= 1 and i>1:               
                ecuacion = ecuacion+"+"+(str(lista_coeficientes[i-1])+variables[i])
            else:
                ecuacion = ecuacion+(str(lista_coeficientes[i-1])+variables[i])
            suma += lista_coeficientes[i-1]*valores[variables[i]]       #se suma el coeficiente multiplicado por el valor de la variable

        #se imprime la ecuación 
        print(f"{ecuacion} = {suma}") 

def verificar_soluciones(valores,variables):   #función que pide y verifica las soluciones del usuario

    soluciones = {}                            #diccionario vacío en el que se guardaran las soluciones dadas
    for i in range(1, len(valores) + 1):
        respuesta = "" 
        while type(respuesta) == str:
            respuesta = input(f"El valor de la variable {variables[i]}: ") #se ingresa la solución
            if respuesta.isnumeric() ==  True or ((respuesta[0] == "-" and respuesta[1].isnumeric() == True) and respuesta.find(".") == False):   #se verifica que el string sea de un numero entero positivo o negativo
                    respuesta = int(respuesta)          
            else:   
                    respuesta = ""  
                    print("El valor de la variable debe ser un número entero")                  
            soluciones[variables[i]] = respuesta                                                                              
    if soluciones == valores:                                                #verificamos si el diccionario original con los valores es igual al nuevo creado
        print("\U0001F600 Solución correcta")                                           #si son iguales, dio la solución correcta
        return (0)
    else:
        print("\U0001F627 Solución incorrecta, los valores correctos son: ")     #si no son iguales, despliega las soluciones
        for i in range(1, len(valores) + 1):
            print(f"{variables[i]} = {valores[variables[i]]}")
        return(1)                                                     #se regresa el valor de 1 en caso de que se haya dado un soluciónn equivocada

def modo_normal():   #función que permite al usuario elegir la cantidad de variables del sistema de ecuaciones y lo presenta.

    variables = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}  #diccionario de variables
    valores = {}  #diccionario vacío con valor de cada variable  
    n = "0"
    while (int(n)<2 or int(n)>8):
        n = input("\nIngrese el número de variables: ")  #pedimos la entrada n
        if n.isnumeric() == False:                       #se verifica si el string puesto es númerico
            n="0"                                        #si no lo es, asigna 0 a n
            print("ERROR. La variable a ingresar debe ser un número entero entre 2 y 8 \U0001F621")  
        elif (int(n)<2 or int(n)>8):                                            #n es númerico pero fuera de rango
            print("ERROR. La variable a ingresar debe ser un número entero entre 2 y 8 \U0001F621")
    n = int(n)    #convertimos a entero el valor de n aceptado

    #random.seed(10)
    for i in range (1,n+1):                   #se crea el diccionario con los valores de cada variable
        valor = random.randint(-10,10)
        valores[variables[i]] = valor

    crear_filas_ecuaciones(n,variables,valores) 
    verificar_soluciones(valores,variables)

def modo_aventura():   #función que permite que el usuario resuelva sistema de ecuaciones de 2 hasta 8 variables.

    variables = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}  #diccionario de variables
    valores = {}  #diccionario vacío con valor de cada variable  
    soluciones_incorrectas = 0   #Variable de la cantidad de soluciones incorrectas
    for n in range(2,9):
        if  soluciones_incorrectas == 3:
            print("\n\U0001F62D Has ingresado 3 soluciones incorrectas, ya no puedes continuar \U0001F62D") #Si se han dado 3 soluciones incorrectas se termina el programa
            break
        else:
            print(f"\nNivel de {n} variables")
            #random.seed(10)
            for i in range (1,n+1):                   #se crea el diccionario con los valores de cada variable
                valor = random.randint(-10,10)
                valores[variables[i]] = valor
            crear_filas_ecuaciones(n,variables,valores) 
            soluciones_incorrectas += verificar_soluciones(valores,variables)   #se recibe un valor y se suma
        if n == 8 and soluciones_incorrectas < 3:
            print("\U0001f600 \U0001F973 ¡FELICIDADES! Lograste completar el programa \U0001F973 \U0001f600")
main()
