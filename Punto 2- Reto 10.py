def productoPunto (*args) -> float: # Definimos la función. 
    listaA = [] # Establecemos lista vacia. 
    listaB = [] # Establecemos lista vacia.  
    resultado = 1 # Establecemos variable.


    for a in range(cantidadNumeros): # Itera. (Desde 0 hasta el valor de la variable)
        numA = int(input("Ingrese valores de la lista A: ")) # Pide ingresar valor numerico. 
        listaA.append(numA) # Agrega valor a la lista.

    for b in range(cantidadNumeros): # Itera. (Desde 0 hasta el valor de la variable)
        numB = int(input("Ingrese numeros de la lista B: ")) # Pide ingresar valor numerico. 
        listaB.append(numB) # Agrega valor a la lista.

    for x in listaA: # Itera la lista. 
        valor1 = x # Guarda valor en variable. 
        for y in listaB: # Itera la lista. 
            valor2 = y # Guarda valor en variable. 
            resultado += (valor1*valor2) # Actualiza. (Suma resultado de productos a los valores guardados en la variable. )

    return ("El punto producto de las 2 listas es: " + str(resultado)) #Devuelve

if __name__ == "__main__": # Inicializa función. 
    cantidadNumeros = int(input("Ingrese la longitud de la listas: ")) # Pide una cantidad de números. 
    print(productoPunto(cantidadNumeros)) # Imprime. 
