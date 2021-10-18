from utilitarios.bienvenida import *
from utilitarios.estilos import *
from manejo_datos.manejo_archivos import *
from algoritmos.dijkstra import *
from algoritmos.imprimir import *
from algoritmos.mostrar_ruta import mostrar_ruta
import msvcrt


def main():
    try:
        bienvenida()

        # Ingresar y leer archivo de texto del grafo 
        nom_archivo = styled_input('Nombre del archivo a leer: ')
        
        grafo = leer_archivo(nom_archivo)

        while True :
            bienvenida()

            # Imprimir lista de adyacencia del grafo
            print_adjacency_list(grafo, 'grafo')
            
            # Ingresar un nodo inicial y verificar si es válido
            inicio = styled_input('\nDigite el nodo inicial: ')
            while inicio == '' or int(inicio) >= len(grafo) or int(inicio) < 0:
                styled_print('rojo', 'Nodo ingresado no válido...')
                inicio = styled_input('\nDigite el nodo inicial: ')
            
            # Generar árbol de búsqueda con el Algoritmo de Dijkstra
            (arbol_busqueda, padres) = dijkstra(grafo, int(inicio))
            
            # Imprimir la lista de adyacencia del árbol de búsqueda generado
            print()
            print_adjacency_list(arbol_busqueda, 'arbol')

            # Generar archivo de texto del árbol de búsqueda generado
            escribir_archivo(arbol_busqueda, inicio)
            styled_print('verde', '\nSe ha creado un archivo con el árbol de búsqueda\n')
            styled_print('verde', 'Pulse una tecla para continuar...', '')
            msvcrt.getwch()

            # Mostrar la ruta más corta del nodo inicial y otro nodo
            mostrar_ruta(arbol_busqueda, padres, inicio)

            # Preguntar si se desea ejecutar nuevamente el programa
            print('\n\n¿Desea encontrar la ruta más corta entre otros nodos?')
            styled_print('verde', '\t\t[1] : Sí', '')
            print('  |  ', end='')
            styled_print('rojo', '[2] : No\n')

            rpta = styled_input('Respuesta: ')

            # Verificar respuesta ingresada
            while rpta == '' or int(rpta) < 1 or int(rpta) > 2:
                styled_print('rojo', 'Respuesta no válida')
                rpta = styled_input('\nRespuesta: ')

            # Respuesta negativa
            if rpta == '2':
                break

    # Si se ingresa un nombre de archivo no válido
    except FileNotFoundError: 
        print('\nAl parecer, el archivo \'', end='')
        styled_print('rojo', str(nom_archivo), '')
        print('\' no existe')
    
    # Si se ingresa un archivo con extensión no válida
    except UnicodeDecodeError:
        print('\nAl parecer, \'', end='')
        styled_print('rojo', str(nom_archivo), '')
        print('\' es un archivo no válido, debe ser ', end='')
        styled_print('azul', '.txt')

    # Si un nodo ingresado no es un un número
    except ValueError:
        styled_print('rojo', '\nError, se ha introducido un valor no válido')
    
    except:
        styled_print('rojo', '\nHa ocurrido un error en el ingreso de datos')

    styled_print('rojo', '\nEl programa ha finalizado')
    styled_print('rojo', 'Pulse una tecla para continuar...', '')
    msvcrt.getch()


if __name__ == '__main__':
    main()