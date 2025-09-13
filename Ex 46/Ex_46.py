funcionarios = {
    "Ana": 2000,
    "Lucas": 2500,
    "Maria": 3000,
    "Pedro": 1800,
    "Carla": 2200
}

for nome, salario in funcionarios.items():
    novo_salario = salario * 1.10
    print(nome, "- Novo salário:", novo_salario)
