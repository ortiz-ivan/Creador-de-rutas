from simbolos import (
    VACIO,
    ENTRADA,
    SALIDA,
    OBSTACULO_USER,
    EDIFICIO,
    AGUA,
    CAMINO,
)
import random


def crear_matriz(columnas, filas):
    return [[VACIO for _ in range(columnas)] for _ in range(filas)]


def es_posicion_dentro(posicion, columnas, filas):
    fila, columna = posicion
    return 0 <= fila < filas and 0 <= columna < columnas


def es_valido(entrada, salida, obstaculo, columnas, filas):
    if not es_posicion_dentro(entrada, columnas, filas):
        return False
    if not es_posicion_dentro(salida, columnas, filas):
        return False
    if not es_posicion_dentro(obstaculo, columnas, filas):
        return False

    if entrada == salida:
        return False
    if obstaculo == entrada or obstaculo == salida:
        return False

    return True


def posicionar_lugares(matriz, entrada, salida):
    fila_e, col_e = entrada
    fila_s, col_s = salida

    matriz[fila_e][col_e] = ENTRADA
    matriz[fila_s][col_s] = SALIDA


def agregar_obstaculo(matriz, obstaculo):
    fila, columna = obstaculo
    matriz[fila][columna] = OBSTACULO_USER


def obstaculos_aleatorios(matriz, cantidad):
    filas = len(matriz)
    columnas = len(matriz[0])
    ocupados = set()

    while len(ocupados) < cantidad:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        if matriz[fila][columna] == VACIO:
            simbolo = random.choice([EDIFICIO, AGUA])
            matriz[fila][columna] = simbolo
            ocupados.add((fila, columna))


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

    posicionar_lugares(matriz, entrada, salida)
    agregar_obstaculo(matriz, obstaculo)
    obstaculos_aleatorios(matriz, cantidad=4)

    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
