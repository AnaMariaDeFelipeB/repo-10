def eliminadorDeCeros (*args) -> int: # Definimos la función. 
    lista = [] # Establecemos lista vacia. 

    for n in range(cantidadNumeros): # Itera. (Desde 0 hasta el valor de la variable)
        num = int(input("Ingresar valor numerico: ")) # Pide ingresar valor numerico. 
        lista.append(num) # Agrega valor a la lista. 
    
    print ("La lista original es: ", lista) # Imprime. 

    totalCeros = lista.count(0)  # Establecemos una variable. (El número de veces que aparece 0)

    for repetidos in lista: # Itera la lista. 
        if repetidos == 0: # Condición: Si el valor es igual a 0 
            lista.remove(0) # Si cumple la condición anterior: Elimina elemento 0) 


    for ceros in range(totalCeros): # Itera. (Desde 0 hasta el valor de la variable)
        lista.append(0) # Agrega 0 a la lista. 
    
    return 'La lista final es:', lista #Devuelve

if __name__ == "__main__": # Inicializa función. 
    cantidadNumeros = int(input("Ingrese la longitud de la lista: ")) # Pide una cantidad de números. 
    print (eliminadorDeCeros(cantidadNumeros)) # Imprime.