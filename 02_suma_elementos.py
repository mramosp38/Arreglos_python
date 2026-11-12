# Programa 2: Suma de elementos
# Lee 5 números enteros, los almacena en una lista y calcula su suma total.

numeros = []
suma_total = 0

# 1. Leer 5 números enteros desde el teclado
for i in range(5):
    num = int(input(f"Ingresa el número {i + 1} de 5: "))
    numeros.append(num)

# 2. Recorrer la lista y acumular la suma de sus elementos
for num in numeros:
    suma_total += num

# 3. Mostrar resultados en consola
print("\nLista ingresada:", numeros)
print("La suma total de los elementos es:", suma_total)