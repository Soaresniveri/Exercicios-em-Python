palavras = ["pastel", "pizza", "banana", "coca-cola", "calabresa"]
palavras_invertidas = []

for palavra in palavras:
   invertida = palavra[::-1]
   palavras_invertidas.append(invertida)

print(palavras_invertidas)