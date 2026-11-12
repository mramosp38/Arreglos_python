# Programa 5: Suma de matrices (bidimensional)
# Lee dos matrices de 2x2, las almacena en listas de listas y calcula su suma.

matriz_a = []
matriz_b = []
matriz_suma = []

# 1. Leer la primera matriz (2x2)
print("--- Ingresa los valores de la Matriz A (2x2) ---")
for i in range(2):
    fila = []
    for j in range(2):
        num = int(input(f"Matriz A [{i}][{j}]: "))
        fila.append(num)
    matriz_a.append(fila)

# 2. Leer la segunda matriz (2x2)
print("\n--- Ingresa los valores de la Matriz B (2x2) ---")
for i in range(2):
    fila = []
    for j in range(2):
        num = int(input(f"Matriz B [{i}][{j}]: "))
        fila.append(num)
    matriz_b.append(fila)

# 3. Calcular la suma posición por posición: C[i][j] = A[i][j] + B[i][j]
for i in range(2):
    fila_suma = []
    for j in range(2):
        suma = matriz_a[i][j] + matriz_b[i][j]
        fila_suma.append(suma)
    matriz_suma.append(fila_suma)

# 4. Mostrar las matrices en consola con formato de tabla
print("\nMatriz A:")
for fila in matriz_a:
    print(fila)

print("\nMatriz B:")
for fila in matriz_b:
    print(fila)

print("\nMatriz Resultante (A + B):")
for fila in matriz_suma:
    print(fila)