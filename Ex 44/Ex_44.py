livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"titulo": "O Alienista", "autor": "Machado de Assis"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado"},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector"}
]

for livro in livros:
    if livro["autor"] == "Machado de Assis":
        print("Título:", livro["titulo"])
