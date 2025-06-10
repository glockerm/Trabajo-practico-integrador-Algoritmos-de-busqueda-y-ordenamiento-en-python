#Funciones
def ordenamiento_por_insercion(lista):
    """Ordena la lista de números de menor a mayor usando el algoritmo de inserción

    Este algoritmo construye la lista ordenada final un elemento a la vez. Recorre
    la lista de entrada y, en cada iteración, toma un elemento y lo inserta en la
    posición correcta dentro de la sublista ya ordenada.

    Parámetros:
        lista: La lista de números desordenada que se desea ordenar.

    Retorna:
        lista: La misma lista de entrada, pero ordenada de menor a mayor. 
    """
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and temp < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = temp
    return lista

def busqueda_binaria(lista,num):
    """Busca un número en la lista previamente ordenada usando búsqueda binaria

    Es un algoritmo eficiente de tipo "divide y vencerás". Funciona dividiendo
    repetidamente el intervalo de búsqueda por la mitad hasta encontrar el
    elemento o determinar que no está en la lista

    Requisito:
        La lista de entrada debe estar ordenada para que el algoritmo funcione correctamente ()

    Parámetros:
        lista: La lista en la que se realizará la búsqueda.
        num: El número que se desea encontrar en la lista

    Retorna:
        int: El índice del número si se encuentra en la lista o si el número no se encuentra, retorna -1
    """
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        # valor del medio
        med = (inicio + fin) // 2
        if lista[med] == num:
            return med
        elif lista[med] < num:
            inicio = med + 1
        else:
            fin = med - 1
    return -1
# Principio del programa
print("Ingrese 10 numeros distintos, estos formaran parte de una lista")
# Lista vacía
lista = []
# Usamos un bucle while que terminará cuando la lista tenga 10 elementos
while len(lista) < 10:
    try:
        numero_ingresado = int(input(f"Ingrese el número {len(lista) + 1}: "))

        # Se verifica si el número ya existe en la lista
        if numero_ingresado in lista:
            # Si ya está, informamos al usuario y el bucle vuelve a empezar.
            print(f"ERROR, el numero {numero_ingresado} ya fue ingresado. Intente con otro.")
        else:
            # Si no está, lo agregamos a la lista.
            lista.append(numero_ingresado)
    # Se imprime esto si lo que se ingresa es diferente de un numero entero o si se ingresa un numero que ya está en la lista.
    except ValueError:
        print("ERROR, ingrese solo numeros enteros")
# Se define variable lista_ordenada como una lista modificada por una función
lista_ordenada = ordenamiento_por_insercion(lista)
print(f"\nLa lista ordenada de menor a mayor es:\n{lista_ordenada}")
# Se pide al usuario un numero de la lista
numero = int(input("\nAhora, ingrese un numero de la lista para encontrar su posición exacta: "))
# se define variable posicion con el retorno de la funcion busqueda_binaria
posicion = busqueda_binaria(lista_ordenada,numero)
# Condicional que evalua si el numero esta o no en la lista
if posicion == -1:
    print("El numero no se encuentra en la lista")
else: 
    print(f"Su posicion exacta es la {posicion}")