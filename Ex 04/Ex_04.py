numeros = [1, 2, 3, 4, 5 , 6, 7, 8]
novos_numero = []

for numero in numeros:
    if numero % 2 == 0:
        novos_numero.append(numero)
        print(numero)