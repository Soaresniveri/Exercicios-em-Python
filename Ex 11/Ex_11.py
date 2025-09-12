numeros = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
negativos = 0

for numero in numeros:
    if numero < 0:
        negativos = negativos + numero
        
print(negativos)