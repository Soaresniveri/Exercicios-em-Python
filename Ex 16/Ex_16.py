numeros = [10, 15, 17, 18, 25, 12, 33, 41, 99, 101]

nm_pares = []
nm_primos = []

for numero in numeros:
    if numero % 2 == 0:
        nm_pares.append(numero)
    else: nm_primos.append(numero)

print(nm_pares)
print(nm_primos)