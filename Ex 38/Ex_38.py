cidades = {
    "São Paulo": 12000000,
    "Rio de Janeiro": 6700000,
    "Campinas": 1200000,
    "Taubaté": 300000,
    "Rezende": 150000
}

for cidade, populacao in cidades.items():
    if populacao > 1000000:
        print(cidade, "-", populacao)
