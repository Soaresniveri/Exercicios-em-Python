produtos = {
    "Arroz": 25,
    "Feijão": 10,
    "Carne": 50,
    "Leite": 6,
    "Pão": 12
}

total = 0
for preco in produtos.values():
    total += preco

print("Total da compra:", total)
