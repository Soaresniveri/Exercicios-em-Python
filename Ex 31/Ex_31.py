cs = {
    "estados": ["São Paulo", "Rio de Janeiro", "Nordeste"],
    "cidades": ["Aparecida", "Rezende", "Canudos"]
    }

for cidade, estado in zip(cs["cidades"], cs["estados"]):
    print(f"Cidade: {cidade} - Estado: {estado}")