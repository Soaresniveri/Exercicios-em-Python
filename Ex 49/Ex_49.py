paises = {
    "Brasil": {"capital": "Brasília", "populacao": 213_000_000},
    "Argentina": {"capital": "Buenos Aires", "populacao": 45_000_000},
    "França": {"capital": "Paris", "populacao": 67_000_000},
    "Japão": {"capital": "Tóquio", "populacao": 125_000_000},
    "EUA": {"capital": "Washington", "populacao": 331_000_000}
}

for pais, info in paises.items():
    print(f"A capital de {pais} é {info['capital']}")
