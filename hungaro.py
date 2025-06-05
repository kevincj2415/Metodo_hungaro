def algoritmo_hungaro(matriz_costos):
    from copy import deepcopy

    trabajadores = len(matriz_costos)
    tareas = len(matriz_costos[0])

    # Asegurarse de que la matriz sea cuadrada: agregar filas o columnas ficticias si es necesario
    if trabajadores < tareas:
        for _ in range(tareas - trabajadores):
            matriz_costos.append([0] * tareas)
    elif trabajadores > tareas:
        for fila in matriz_costos:
            fila.extend([0] * (trabajadores - tareas))

    n = len(matriz_costos)
    matriz = deepcopy(matriz_costos)

    # Paso 1: Resta mínima por fila
    for i in range(n):
        minimo_fila = min(matriz[i])
        matriz[i] = [valor - minimo_fila for valor in matriz[i]]

    # Paso 2: Resta mínima por columna
    for j in range(n):
        columna = [matriz[i][j] for i in range(n)]
        minimo_columna = min(columna)
        for i in range(n):
            matriz[i][j] -= minimo_columna

    def encontrar_ceros(m):
        return [(i, j) for i in range(n) for j in range(n) if m[i][j] == 0]

    def cubrir_ceros(m):
        fila_cubierta = [False] * n
        columna_cubierta = [False] * n
        marcado = [[0]*n for _ in range(n)]
        ceros = encontrar_ceros(m)
        fila_tiene_estrella = [False] * n
        columna_tiene_estrella = [False] * n

        for i, j in ceros:
            if not fila_tiene_estrella[i] and not columna_tiene_estrella[j]:
                marcado[i][j] = 1
                fila_tiene_estrella[i] = True
                columna_tiene_estrella[j] = True

        for j in range(n):
            for i in range(n):
                if marcado[i][j] == 1:
                    columna_cubierta[j] = True

        return marcado, fila_cubierta, columna_cubierta

    def paso4(matriz, marcado, fila_cubierta, columna_cubierta):
        while True:
            cero_encontrado = False
            for i in range(n):
                for j in range(n):
                    if matriz[i][j] == 0 and not fila_cubierta[i] and not columna_cubierta[j]:
                        marcado[i][j] = 2
                        columna_con_estrella = next((k for k in range(n) if marcado[i][k] == 1), -1)
                        if columna_con_estrella != -1:
                            fila_cubierta[i] = True
                            columna_cubierta[columna_con_estrella] = False
                        else:
                            return aumentar_camino(marcado, i, j)
                        cero_encontrado = True
                        break
                if cero_encontrado:
                    break
            else:
                return None

    def aumentar_camino(marcado, fila, columna):
        camino = [(fila, columna)]
        while True:
            f = next((i for i in range(n) if marcado[i][columna] == 1), None)
            if f is None:
                break
            camino.append((f, columna))
            c = next((j for j in range(n) if marcado[f][j] == 2), None)
            if c is None:
                break
            camino.append((f, c))
            fila, columna = f, c

        for f, c in camino:
            if marcado[f][c] == 1:
                marcado[f][c] = 0
            elif marcado[f][c] == 2:
                marcado[f][c] = 1

        for i in range(n):
            for j in range(n):
                if marcado[i][j] == 2:
                    marcado[i][j] = 0

        return True

    def ajustar_matriz(matriz, fila_cubierta, columna_cubierta):
        minimo_no_cubierto = min(
            matriz[i][j]
            for i in range(n)
            for j in range(n)
            if not fila_cubierta[i] and not columna_cubierta[j]
        )

        for i in range(n):
            for j in range(n):
                if fila_cubierta[i]:
                    matriz[i][j] += minimo_no_cubierto
                if not columna_cubierta[j]:
                    matriz[i][j] -= minimo_no_cubierto

    while True:
        marcado, fila_cubierta, columna_cubierta = cubrir_ceros(matriz)

        while sum(columna_cubierta) < n:
            resultado = paso4(matriz, marcado, fila_cubierta, columna_cubierta)
            if not resultado:
                ajustar_matriz(matriz, fila_cubierta, columna_cubierta)
            else:
                break

        estrellas = [(i, j) for i in range(n) for j in range(n) if marcado[i][j] == 1]
        if len(estrellas) == n:
            asignacion = [0] * n
            for i, j in estrellas:
                asignacion[i] = j

            # Limitar asignación a los trabajadores reales
            asignacion = asignacion[:trabajadores]

            # Calcular costo total real (solo para los trabajadores reales)
            costo_total = sum(
                matriz_costos[i][asignacion[i]]
                for i in range(trabajadores)
            )

            return asignacion, costo_total
