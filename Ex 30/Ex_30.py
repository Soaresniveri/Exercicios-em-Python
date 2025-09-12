palavras = ["Pancreas", "Ponei", "Olho", "Banana", "Top"]
palavras_com_P = []
for palavra in palavras:
    primeira_letra = palavra[0]
    if primeira_letra.upper() == "P":
        palavras_com_P.append(palavra)

print(palavras_com_P)