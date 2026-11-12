# Programa 3: Encontrar número mayor y menor
# Lee 8 números enteros, los almacena en una lista y determina el mayor y el menor.

numeros = []

# 1. Leer 8 números enteros desde el teclado
for i in range(8):
    num = int(input(f"Ingresa el número {i + 1} de 8: "))
    numeros.append(num)

# 2. Inicializar mayor y menor con el primer elemento de la lista
mayor = numeros[0]
menor = numeros[0]

# 3. Recorrer la lista para comparar cada elemento
for num in numeros:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

# 4. Mostrar resultados en consola
print("\nLista ingresada:", numeros)
print("El número mayor es:", mayor)
print("El número menor es:", menor)