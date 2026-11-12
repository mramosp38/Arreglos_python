# Programa 1: Contar números pares e impares
# Lee 10 números enteros, los guarda en una lista y cuenta pares e impares.

numeros = []
pares = 0
impares = 0

# 1. Leer 10 números enteros desde el teclado
for i in range(10):
    num = int(input(f"Ingresa el número {i + 1} de 10: "))
    numeros.append(num)

# 2. Recorrer la lista y contar pares e impares
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# 3. Mostrar resultados en consola
print("\nLista ingresada:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)