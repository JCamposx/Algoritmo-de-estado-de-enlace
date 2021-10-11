from utilitarios.estilos import *


# Imprimir la lista de adyacencia de un arbol de busqueda
def print_adjacency_list(dic, tipo):
    if tipo == 'grafo':
        styled_print('azul', 'Lista de adyacencia del grafo:\n')
    else :
        styled_print('azul', 'Lista de adyacencia del árbol de búsqueda:\n')

    for key in dic:
        print(key, ':', dic[key])
    
    if tipo == 'grafo':
        styled_print('amarillo', 'nodo : [[vecino, peso], ...]')
    else :
        styled_print('amarillo', 'nodo : [[vecinos], peso_acumulado]')