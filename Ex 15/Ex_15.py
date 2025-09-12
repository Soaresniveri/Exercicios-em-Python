nomes = ["Lucas", "Murilo", "Daniel", "Ana", "Rafael", "Pedro", "Julio", "Jesus", "Moises", "Noé"]
cont = 0

while cont < len(nomes):
    nome_atual = nomes[cont]

    if nome_atual == "Ana":
        break

    print(nome_atual)
    cont += 1