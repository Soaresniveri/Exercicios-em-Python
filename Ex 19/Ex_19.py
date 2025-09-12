numeros = [1,2,3,4,5,6,7,8,9,10]
numeros_pares = []
media = 0
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

media = sum(numeros_pares) / len(numeros_pares)

print(numeros_pares)
print(media)