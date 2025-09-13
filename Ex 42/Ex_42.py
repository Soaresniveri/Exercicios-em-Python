alunos = {
    "João": [8.5, 9.0],
    "Maria": [7.0, 6.5],
    "Pedro": [10.0, 9.5]
}

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")
