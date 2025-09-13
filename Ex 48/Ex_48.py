produto = {
    "nome": "Notebook",
    "preco": 3500,
    "disponivel": True
}

for chave, valor in produto.items():
    if chave == "disponivel":
        if valor:
            print(f"O produto {produto['nome']} está disponível")
        else:
            print(f"O produto {produto['nome']} está indisponível")
