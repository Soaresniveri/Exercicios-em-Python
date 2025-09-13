frutas = {
    "Banana": "Amarela",
    "Maçã": "Vermelha",
    "Uva": "Roxa",
    "Laranja": "Laranja",
    "Abacate": "Verde"
}

# adicionando uma nova fruta
frutas["Pera"] = "Verde"

for fruta, cor in frutas.items():
    print(fruta, "-", cor)
