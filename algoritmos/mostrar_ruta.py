from utilitarios.estilos import *
from utilitarios.bienvenida import *
from algoritmos.imprimir import *

# Mostrar la ruta desde un nodo hacia otro
def mostrar_ruta(arbol, padre, inicio):
    bienvenida()
    
    print_adjacency_list(arbol, 'arbol')

    print('\nNodo inicial: ', end='')
    styled_print('cyan', inicio)

    fin = int(verificar_ingreso(arbol))

    if fin == int(inicio):
        styled_print('amarillo', '\nHa ingresado el nodo inicial')
        print('Peso acumulado: ', end='')
        styled_print('amarillo', '0')
    else:
        ruta = calcular_ruta_raiz(fin, padre)
        print_ruta(inicio, fin, ruta, arbol)


# Verificamos si el nodo ingresado es válido o no
def verificar_ingreso(arbol):
    dato = styled_input('\nNodo final: ')

    while dato == '' or int(dato) >= len(arbol) or int(dato) < 0:
        styled_print('rojo', 'Nodo ingresado no válido...')
        dato = styled_input('\nNodo de fin: ')
    
    return dato


# Calcular la ruta desde un nodo hasta la raiz
def calcular_ruta_raiz(nodo, padre):
    ruta = []

    while nodo != -1:
        ruta.append(nodo)
        nodo = padre[nodo]

    ruta.reverse()

    return ruta


# Imprimir la ruta entre 2 nodos
def print_ruta(inicio, fin, ruta, arbol):
    print('\n\nRuta desde el nodo ', end='')
    styled_print('morado', str(inicio), '')
    print(' hasta el nodo ', end='')
    styled_print('morado', str(fin), '')
    print(':\n')
    styled_print('morado', str(inicio), '')

    for i in range(1,len(ruta)-1):
        styled_print('amarillo', ' -> ', '')
        print(ruta[i], end='')

    styled_print('amarillo', ' -> ', '')
    styled_print('morado', str(fin))

    print('\nPeso acumulado: ', end='')
    styled_print('amarillo', str(arbol[fin][1]))
