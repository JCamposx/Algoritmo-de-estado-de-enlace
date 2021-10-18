colores = {
        'rojo' : '\033[1;31m',
        'verde' : '\033[1;32m',
        'amarillo' : '\033[1;33m',
        'azul' : '\033[1;34m',
        'morado' : '\033[1;35m',
        'cyan' : '\033[1;36m',
        'reset' : '\033[0m',
    }


# Imprimir con colores
def styled_print(color, msg, end_=None):
    if end_ is None:
        print(colores[color] + msg + colores['reset'])
    else:
        print(colores[color] + msg + colores['reset'], end='')


# Mostrar lo que ingrese el usuario de otro color
def styled_input(msg):
    print(msg, end='' + colores['cyan'])

    dato = input()

    print(colores['reset'], end='')

    return dato