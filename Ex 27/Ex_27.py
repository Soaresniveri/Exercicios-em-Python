numeros = [12, 5, 8, 3, 9, 15, 6, 10, 7, 4]
numeros.sort()
tamanho = len(numeros)
if tamanho % 2 == 0:
    meio1 = numeros[tamanho//2 - 1]
    meio2 = numeros[tamanho//2]
    mediana = (meio1 + meio2) / 2
else:
    mediana = numeros[tamanho//2]

print("Lista ordenada:", numeros)
print("Mediana:", mediana)
