pessoas = {
    "Ana": 25,
    "Lucas": 35,
    "Maria": 40,
    "Pedro": 28,
    "Carla": 50
}

mais_de_30 = []
for nome, idade in pessoas.items():
    if idade > 30:
        mais_de_30.append(nome)

print("Pessoas com mais de 30 anos:", mais_de_30)
