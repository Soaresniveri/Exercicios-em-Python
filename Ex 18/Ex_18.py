numeros = [10,10,20,20,25,30,30,40,40,45,50,50,55,60,60,65,70]

numeros_unicos = []

for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

print(numeros_unicos)