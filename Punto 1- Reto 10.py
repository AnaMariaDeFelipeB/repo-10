def promedioReales (*args) ->float: # Definimos la función. 
    lista = [] # Establecemos lista vacia. 
    suma = 0 # Establecemos variable. 

    for n in range(cantidadNumeros): # Itera. (Desde 0 hasta el valor de la variable)
        num = float(input("Ingrese número: ")) # Pide ingresar valor numerico. 
        lista.append(num) # Agrega valor a la lista. 
        
    for numeros in lista: # Itera la lista. 
        suma = suma + numeros # Suma cada valor de la lista. 
    
    return (round((suma/len(lista)), 4)) # Devuelve valor.

if __name__ == "__main__": # Inicializa función. 
    cantidadNumeros = int(input("Ingrese cantidad de números: ")) # Pide una cantidad de números. 
    print("El promedio es: ", promedioReales(cantidadNumeros)) # Imprime comentario y valor de la variable. 