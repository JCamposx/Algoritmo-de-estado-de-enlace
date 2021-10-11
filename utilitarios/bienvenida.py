from utilitarios.estilos import *
import os


def bienvenida():
    os.system('cls')
    
    a = 'ALGORITMO ESTADO DE ENLACE'
    styled_print('verde',
        '-' * (len(a) + 6) + '\n'
        '-- ' + a + ' --\n' +
        '-' * (len(a) + 6) + '\n'
    )