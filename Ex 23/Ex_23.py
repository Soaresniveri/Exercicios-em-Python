numeros1 = [1,2,3,4,5]
numeros2 = [6,7,8,9,10]

nm_mult = []

for numero1 in numeros1:
    for numero2 in numeros2:
        mult = numero1 * numero2
        nm_mult.append(mult)

print(nm_mult)