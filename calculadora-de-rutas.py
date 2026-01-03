import random


def crear_matriz(columnas, filas):
    matriz = [["." for _ in range(columnas)] for _ in range(filas)]
    return matriz


def es_valido(entrada, salida, obstaculo, columnas, filas):
    for fila, columna in (entrada, salida, obstaculo):
        if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
            return False

    if entrada == salida:
        return False
    if obstaculo == entrada or obstaculo == salida:
        return False

    return True


def posicionar_lugares(matriz, entrada, salida, obstaculo):
    fila_entrada, col_entrada = entrada
    fila_salida, col_salida = salida
    fila_obs, col_obs = obstaculo

    matriz[fila_entrada][col_entrada] = "E"
    matriz[fila_salida][col_salida] = "S"
    matriz[fila_obs][col_obs] = "X"


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))


def main():
    columnas = 5
    filas = 5
    matriz = crear_matriz(columnas, filas)
    entrada = (0, 0)
    salida = (4, 4)
    obstaculo = (2, 2)
    if not es_valido(entrada, salida, obstaculo, columnas, filas):
        print("Posiciones inválidas")
        return
    posicionar_lugares(matriz, entrada, salida, obstaculo)
    imprimir_matriz(matriz)


main()
