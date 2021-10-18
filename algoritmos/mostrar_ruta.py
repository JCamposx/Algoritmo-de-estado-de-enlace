from utilitarios.estilos import *
from utilitarios.bienvenida import *
from algoritmos.imprimir import *

# Mostrar la ruta desde un nodo hacia otro
def mostrar_ruta(arbol, padre, inicio):
    bienvenida()
    
    # Imprimir árbol de búsqueda
    print_adjacency_list(arbol, 'arbol')

    # Imprimir nodo inicial
    print('\nNodo inicial: ', end='')
    styled_print('cyan', inicio)

    # Ingresar nodo final y verfificar si es válido
    fin = int(verificar_ingreso(arbol))

    # Verificar si el nodo final ingresado es el nodo inicial
    if fin == int(inicio):
        styled_print('amarillo', '\nHa ingresado el nodo inicial')
        print('Peso acumulado: ', end='')
        styled_print('amarillo', '0')
    else:
        # Calcular la ruta hasta la raiz del árbol e imprimirla
        ruta = calcular_ruta_raiz(fin, padre)
        print_ruta(inicio, fin, ruta, arbol)


# Verificamos si el nodo ingresado es válido o no
def verificar_ingreso(arbol):
    # Ingresar el nodo final
    dato = styled_input('\nNodo final: ')

    # Verificar si el nodo final es válido
    while dato == '' or int(dato) >= len(arbol) or int(dato) < 0:
        styled_print('rojo', 'Nodo ingresado no válido...')
        dato = styled_input('\nNodo de fin: ')
    
    return dato


# Calcular la ruta desde un nodo hasta la raiz
def calcular_ruta_raiz(nodo, padre):
    ruta = []

    # Mientras el nodo sea diferente a -1
    while nodo != -1:
        # Agregamos el nodo a ruta
        ruta.append(nodo)

        # Cambiamos el valor de nodo por su padre
        nodo = padre[nodo]

    # Invertimos ruta
    ruta.reverse()

    return ruta


# Imprimir la ruta entre 2 nodos
def print_ruta(inicio, fin, ruta, arbol):
    print('\n\nRuta más corta desde el nodo ', end='')
    styled_print('morado', str(inicio), '')
    print(' hasta el nodo ', end='')
    styled_print('morado', str(fin), '')
    print(':\n')
    styled_print('morado', str(inicio), '')

    # Recorrer la ruta e imprimir cada nodo
    for i in range(1,len(ruta)-1):
        styled_print('amarillo', ' -> ', '')
        print(ruta[i], end='')

    styled_print('amarillo', ' -> ', '')
    styled_print('morado', str(fin))

    # Imprimir peso acumulado
    print('\nPeso acumulado: ', end='')
    styled_print('amarillo', str(arbol[fin][1]))
