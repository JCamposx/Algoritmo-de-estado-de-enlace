import math


# Ejecutar el algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    # Definimos el arbol de busqueda a encontrar
    arbol = {x : [[], None] for x in grafo}
    arbol[inicio][1] = 0

    # Definimos la cola de nodos por visitar
    cola = [inicio]

    # Definimos un arreglo de nodos que han sido visitados
    visitado = [0 for x in grafo]
    visitado[inicio] = 1

    # Definimos un arreglo de saltos acumulados hasta un nodo
    saltos_acum = [0 for x in grafo]

    # Definimos un arreglo de peso aumulado hasta un nodo
    peso_acum = [math.inf for x in grafo]
    peso_acum[inicio] = 0

    # Definimos un arreglo de padres de cada nodo
    padre = [-1 for x in grafo]

    # Mientras la cola tenga elementos
    while len(cola) > 0:
        inicio = cola[0]
        for vecino in grafo[inicio]:
            nodo = vecino[0]                     # nodo vecino
            peso = peso_acum[inicio] + vecino[1] # peso total hasta el nodo vecino
            saltos = saltos_acum[inicio] + 1     # saltos totales hasta el nodo vecino

            if nodo != padre[inicio]:
                
                # Si encontramos una ruta con menor peso, o con menor peso y que tome menos saltos en llegar
                if peso < peso_acum[nodo] or (peso == peso_acum[nodo] and saltos < saltos_acum[nodo]):

                    # Si el nodo vecino ya ha sido visitado
                    if visitado[nodo] == 1:

                        # Quitamos la relacion en el árbol de búsqueda por encontrar
                        arbol[padre[nodo]][0].remove(nodo)
                        arbol[nodo][0].remove(padre[nodo])

                        # Si el nodo vecino se encuentra en la cola, lo quitamos
                        if nodo in cola:
                            cola.remove(nodo)
                    
                    # Deffinimos el padre del nodo vecino
                    padre[nodo] = inicio

                    # Actualizamos los arreglos de peso y saltos acumulados del nodo vecino
                    peso_acum[nodo] = peso
                    saltos_acum[nodo] = saltos

                    # Agregamos la relacion al árbol de búsqueda por encontrar
                    arbol[inicio][0].append(nodo)
                    arbol[nodo][0].append(padre[nodo])
                    arbol[nodo][1] = peso_acum[nodo]

                    # Encolamos el nodo vecino
                    cola.append(nodo)

            # Marcamos el nodo vecino como visitado
            visitado[nodo] = 1
        
        # Decolamos la cola
        cola.pop(0)

    return (arbol, padre)