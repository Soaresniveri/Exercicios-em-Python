hobbies = {
    "Ana": ["leitura", "natação"],
    "Lucas": ["futebol", "videogame"],
    "Maria": ["dança", "leitura"],
    "Pedro": ["corrida", "xadrez"],
    "Carla": ["leitura", "música"]
}

for nome, lista in hobbies.items():
    if "leitura" in lista:
        print(nome, "gosta de leitura")
