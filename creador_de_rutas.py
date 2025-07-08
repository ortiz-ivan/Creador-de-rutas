from collections import deque
import random

# Creacion del mapa de acuerdo a los inputs
filas = int(input("Ingrese número de filas:\n"))
columnas = int(input("Ingrese número de columnas:\n"))
mapa = [["." for _ in range(columnas)] for _ in range(filas)]
capacidad_total = filas * columnas


# Imprime el mapa
def imprimir_mapa(mapa):
    for fila in mapa:
        print(" ".join(fila))


# Calcula una cantidad aleatoria de obstáculos (edificios y agua), asegurándose de no superar el 30% del tamaño total del mapa
max_obstaculos = int(capacidad_total * 0.3)
cantidad_edificios = random.randint(
    int(capacidad_total * 0.1), int(capacidad_total * 0.2)
)  # Los edificios y el agua se generan en rangos entre el 10% y 20% del mapa
cantidad_agua = random.randint(int(capacidad_total * 0.1), int(capacidad_total * 0.2))

if cantidad_edificios + cantidad_agua > max_obstaculos:
    cantidad_agua = max_obstaculos - cantidad_edificios

print(f"\nCantidad aleatoria de edificios: {cantidad_edificios}")
print(f"Cantidad aleatoria de agua: {cantidad_agua}")

ocupados = set()
# Genera coordenadas aleatorias para edificios y cuerpos de agua
edificios = []
while len(edificios) < cantidad_edificios:
    f = random.randint(0, filas - 1)
    c = random.randint(0, columnas - 1)
    if (f, c) not in ocupados:
        edificios.append((f, c))
        ocupados.add((f, c))
# Se utiliza un conjunto 'ocupados' para asegurarse de que cada celda tenga un solo tipo de obstáculo.
agua = []
while len(agua) < cantidad_agua:
    f = random.randint(0, filas - 1)
    c = random.randint(0, columnas - 1)
    if (f, c) not in ocupados:
        agua.append((f, c))
        ocupados.add((f, c))

for fila, columna in edificios:
    mapa[fila][columna] = "#"

for fila, columna in agua:
    mapa[fila][columna] = "@"

imprimir_mapa(mapa)

obstaculos_usuario = []


# Pide al usuario si quiere agregar un obstaculo si es asi, valida que sea dentro del mapa y verifica si la coordenada se encuentra o no sobre un obstaculo
def agregar_obstaculo(mapa, filas, columnas, ocupados):
    while True:
        obstaculo = int(
            input("Ingrese 1 si desea agregar un obstáculo, 0 para continuar:\n")
        )
        if obstaculo == 1:
            obstaculo_fila = int(input("Ingrese la fila de su obstáculo:\n"))
            obstaculo_columna = int(input("Ingrese la columna de su obstáculo:\n"))
            nuevo_obstaculo = (obstaculo_fila, obstaculo_columna)

            if not (0 <= obstaculo_fila < filas and 0 <= obstaculo_columna < columnas):
                print("Coordenada fuera del mapa.")
            elif nuevo_obstaculo in ocupados:
                print(f"La coordenada ya está ocupada: {nuevo_obstaculo}")
            else:
                obstaculos_usuario.append(nuevo_obstaculo)
                ocupados.add(nuevo_obstaculo)
                mapa[obstaculo_fila][obstaculo_columna] = "X"
                print("Obstáculo agregado.")
                imprimir_mapa(mapa)
        elif obstaculo == 0:
            break


for fila, columna in obstaculos_usuario:
    mapa[fila][columna] = "X"

# Entrada y salida
while True:
    entrada_fila = int(input("Ingrese la fila de entrada:\n"))
    entrada_columna = int(input("Ingrese la columna de entrada:\n"))
    salida_fila = int(input("Ingrese la fila de salida:\n"))
    salida_columna = int(input("Ingrese la columna de salida:\n"))

    entrada = (entrada_fila, entrada_columna)
    salida = (salida_fila, salida_columna)
    # Valida que las coordenadas ingresadas no esten fuera del mapa
    coordenadas_validas = (
        0 <= entrada_fila < filas
        and 0 <= entrada_columna < columnas
        and 0 <= salida_fila < filas
        and 0 <= salida_columna < columnas
    )

    if not coordenadas_validas:
        print("Entrada o salida fuera del mapa. Intente de nuevo.\n")
        continue
    # Verifica que las coordenadas de entrada y salida no esten sobre un obstaculo
    if entrada in ocupados:
        print(f"La entrada {entrada} está sobre un obstáculo. Intente de nuevo.\n")
        continue

    if salida in ocupados:
        print(f"La salida {salida} está sobre un obstáculo. Intente de nuevo.\n")
        continue

    mapa[entrada_fila][entrada_columna] = "E"
    mapa[salida_fila][salida_columna] = "S"
    break


def bfs_mapa(mapa):
    # Inicializa la cola con una tupla: (posición actual, camino recorrido hasta ahora)
    cola = deque([(entrada, [entrada])])
    visitados = set()
    # Mientras haya nodos por explorar en la cola toma el primer nodo en la cola, si ya fue visitado, lo salta
    while cola:
        (fila, columna), camino = cola.popleft()
        if (fila, columna) in visitados:
            continue
        visitados.add((fila, columna))
        # Si llegó a la salida, retorna el camino completo
        if mapa[fila][columna] == "S":
            return camino
        # Recorre en 4 direcciones, arriba, abajo, izquierda, derecha
        for desplazamiento_fila, desplazamiento_columna in [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]:
            nueva_fila = fila + desplazamiento_fila
            nueva_columna = columna + desplazamiento_columna
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                if mapa[nueva_fila][nueva_columna] in (".", "S"):
                    # Agrega la nueva posición a la cola junto con el camino actualizado
                    cola.append(
                        (
                            (nueva_fila, nueva_columna),
                            camino + [(nueva_fila, nueva_columna)],
                        )
                    )
    return None


# Verifica si se encontro un camino y muestra visualmente el trayecto recorrido
def crear_camino(mapa, camino):
    if camino:
        for fila, columna in camino[1:-1]:
            if mapa[fila][columna] not in ("S", "E"):
                mapa[fila][columna] = "*"
    else:
        print("No se encontró un camino.")


camino = bfs_mapa(mapa)
print("\nCamino encontrado:\n")
crear_camino(mapa, camino)
imprimir_mapa(mapa)


while True:
    print("\n¿Querés agregar un nuevo obstáculo?\n")
    agregar_obstaculo(mapa, filas, columnas, ocupados)

    for f in range(filas):
        for c in range(columnas):
            if mapa[f][c] == "*":
                mapa[f][c] = "."

    camino = bfs_mapa(mapa)
    print("\nMapa actualizado con nuevos obstáculos:\n")
    crear_camino(mapa, camino)
    imprimir_mapa(mapa)

    agregar_obstaculo(mapa, filas, columnas, ocupados)
    break
