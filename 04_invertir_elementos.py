# Programa 4: Invertir elementos
# Lee 6 números enteros, los almacena en una lista e invierte el orden de sus elementos.

numeros = []
lista_invertida = []

# 1. Leer 6 números enteros desde el teclado
for i in range(6):
    num = int(input(f"Ingresa el número {i + 1} de 6: "))
    numeros.append(num)

# 2. Recorrer la lista original desde el último índice hasta el primero
for i in range(len(numeros) - 1, -1, -1):
    lista_invertida.append(numeros[i])

# 3. Mostrar resultados en consola
print("\nLista original:", numeros)
print("Lista invertida:", lista_invertida)