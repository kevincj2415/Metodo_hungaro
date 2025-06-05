def algoritmo_hungaro(matriz_costos):
    # Copiar matriz original
    matriz = [fila[:] for fila in matriz_costos]

    filas = len(matriz)
    columnas = len(matriz[0])

    # Hacer matriz cuadrada agregando ceros
    if filas < columnas:
        for _ in range(columnas - filas):
            matriz.append([0] * columnas)
    elif filas > columnas:
        for fila in matriz:
            fila.extend([0] * (filas - columnas))

    n = len(matriz)

    # Paso 1: restar el número más chico de cada fila
    for i in range(n):
        menor = min(matriz[i])
        for j in range(n):
            matriz[i][j] -= menor

    # Paso 2: restar el menor de cada columna
    for j in range(n):
        col = [matriz[i][j] for i in range(n)]
        menor = min(col)
        for i in range(n):
            matriz[i][j] -= menor

    # Encontrar los ceros en la matriz
    def buscar_ceros(m):
        lista = []
        for i in range(n):
            for j in range(n):
                if m[i][j] == 0:
                    lista.append((i, j))
        return lista

    # Cubrir ceros con líneas (básicamente marcar)
    def marcar_ceros(m):
        filas_marcadas = [False] * n
        columnas_marcadas = [False] * n
        marcas = [[0] * n for _ in range(n)]
        usados_filas = [False] * n
        usados_columnas = [False] * n

        ceros = buscar_ceros(m)

        for i, j in ceros:
            if not usados_filas[i] and not usados_columnas[j]:
                marcas[i][j] = 1  # estrella
                usados_filas[i] = True
                usados_columnas[j] = True

        for i in range(n):
            for j in range(n):
                if marcas[i][j] == 1:
                    columnas_marcadas[j] = True

        return marcas, filas_marcadas, columnas_marcadas

    # Paso 4: manejar los ceros no cubiertos
    def paso_cuatro(m, marcas, filas_marcadas, columnas_marcadas):
        while True:
            cero_encontrado = False
            for i in range(n):
                for j in range(n):
                    if m[i][j] == 0 and not filas_marcadas[i] and not columnas_marcadas[j]:
                        marcas[i][j] = 2  # primo
                        hay_estrella = False
                        for k in range(n):
                            if marcas[i][k] == 1:
                                filas_marcadas[i] = True
                                columnas_marcadas[k] = False
                                hay_estrella = True
                                break
                        if not hay_estrella:
                            return cambiar_marcas(marcas, i, j)
                        cero_encontrado = True
                        break
                if cero_encontrado:
                    break
            else:
                return None

    # Cambiar camino alternante
    def cambiar_marcas(marcas, fila, col):
        camino = [(fila, col)]

        while True:
            f = None
            for i in range(n):
                if marcas[i][col] == 1:
                    f = i
                    break
            if f is None:
                break
            camino.append((f, col))

            c = None
            for j in range(n):
                if marcas[f][j] == 2:
                    c = j
                    break
            if c is None:
                break
            camino.append((f, c))
            fila, col = f, c

        for f, c in camino:
            if marcas[f][c] == 1:
                marcas[f][c] = 0
            elif marcas[f][c] == 2:
                marcas[f][c] = 1

        for i in range(n):
            for j in range(n):
                if marcas[i][j] == 2:
                    marcas[i][j] = 0

        return True

    # Si no hay suficientes ceros, ajustar la matriz
    def cambiar_matriz(m, filas_marcadas, columnas_marcadas):
        min_valor = None
        for i in range(n):
            for j in range(n):
                if not filas_marcadas[i] and not columnas_marcadas[j]:
                    if min_valor is None or m[i][j] < min_valor:
                        min_valor = m[i][j]

        for i in range(n):
            for j in range(n):
                if filas_marcadas[i]:
                    m[i][j] += min_valor
                if not columnas_marcadas[j]:
                    m[i][j] -= min_valor

    while True:
        marcas, filas_marcadas, columnas_marcadas = marcar_ceros(matriz)

        while sum(columnas_marcadas) < n:
            resultado = paso_cuatro(matriz, marcas, filas_marcadas, columnas_marcadas)
            if not resultado:
                cambiar_matriz(matriz, filas_marcadas, columnas_marcadas)
            else:
                break

        # Ver si ya se hizo la asignación completa
        estrellas = []
        for i in range(n):
            for j in range(n):
                if marcas[i][j] == 1:
                    estrellas.append((i, j))

        if len(estrellas) == n:
            asignacion = [0] * n
            for i, j in estrellas:
                asignacion[i] = j

            asignacion = asignacion[:filas]
            costo = 0
            for i in range(filas):
                costo += matriz_costos[i][asignacion[i]]

            return asignacion, costo
