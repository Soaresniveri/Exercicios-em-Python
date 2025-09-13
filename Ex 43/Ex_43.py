frase = "banana amarela"
frequencia = {}

for letra in frase:
    if letra != " ":  # ignorar espaços
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

print("Frequência de letras:", frequencia)
