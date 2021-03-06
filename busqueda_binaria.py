import random
import time

# Ejemplo de busqueda dentro de una lista.
def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

mi_lista = [1, 3, 5 , 10, 12]

print(busqueda_ingenua(mi_lista, 10))

def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # Inicio de a lista.
    if limite_superior is None:
        limite_superior = len(lista) - 1 # Final de la lista.

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)



if __name__=='__main__':

    # Crear lista con 10.000 elementos.
    tamano = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamano:
        conjunto_inicial.add(random.randint(-3*tamano, +3*tamano))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir tiempo de busqueda ingenua.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")

    # Medir tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")


# Comparación en ambas funciones en mi PC:
# Tiempo de busqueda ingenua: 2.19700026512146 segundos.
# Tiempo de busqueda binaria: 0.04500007629394531 segundos.