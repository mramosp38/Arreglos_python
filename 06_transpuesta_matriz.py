# Programa 6: Transpuesta de una matriz (bidimensional)
# Lee una matriz de 3x3, la almacena en una lista de listas y calcula su transpuesta.

matriz = []
transpuesta = []

# 1. Leer la matriz original de 3x3 (9 números)
print("--- Ingresa los valores de la Matriz (3x3) ---")
for i in range(3):
    fila = []
    for j in range(3):
        num = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(num)
    matriz.append(fila)

# 2. Calcular la transpuesta (intercambiar filas por columnas)
for i in range(3):
    fila_transpuesta = []
    for j in range(3):
        # Tomamos el elemento de la columna i y fila j: matriz[j][i]
        fila_transpuesta.append(matriz[j][i])
    transpuesta.append(fila_transpuesta)

# 3. Mostrar la matriz original y la transpuesta en consola
print("\nMatriz Original (3x3):")
for fila in matriz:
    print(fila)

print("\nMatriz Transpuesta (3x3):")
for fila in transpuesta:
    print(fila)