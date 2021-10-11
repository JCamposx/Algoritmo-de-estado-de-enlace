# Abrir un archivo y pasamos sus datos a un diccionario
def leer_archivo(nom_archivo):
    dic = {}

    with open(nom_archivo) as archivo:
        valor = []
        for linea in archivo:
            (key, valor) = linea.split(' -> ')
            lista = valor.split(' ; ')
            matriz = []
            for elemento in lista:
                n = elemento.split('-')
                r = [int(x) for x in n]
                matriz.append(r)
            dic[int(key)] = matriz
    
    archivo.close()

    return dic


# Crear un archivo con la lista de adyacencia de un árbol de búsqueda
def escribir_archivo(arbol_busqueda, nodo):
    nombre = 'arbol_nodo_' + str(nodo) + '.txt'
    archivo = open(nombre, 'w')

    archivo.write('ARBOL DE BUSQUEDA DEL NODO ' + str(nodo) + '\n\n')

    for key in arbol_busqueda:
        nodo = str(key)
        vecinos = str(arbol_busqueda[key][0])
        peso_acum = str(arbol_busqueda[key][1])
        
        archivo.write(nodo + ' -> vecinos: ' + vecinos + '\n\t peso acumulado: ' + peso_acum + ' \n\n')
    
    archivo.close()