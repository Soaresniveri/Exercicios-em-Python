estoque = {
    "Arroz": 5,
    "Feijão": 15,
    "Macarrão": 8,
    "Carne": 20,
    "Leite": 3
}

for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(produto, "- Estoque baixo!")
