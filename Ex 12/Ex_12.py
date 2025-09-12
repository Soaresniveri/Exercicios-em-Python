palavras = ["Banana", "Anjo", "Urso", "Cachorro", "Cavalo"]
cont_vogal = 0

for palavra in palavras:    # Percorre cada palavra
    for letra in palavra:   # Percorre cada letra
        if letra in "aeiouAEIOU": #Verifica se ha vogal na palavra
         cont_vogal += 1 #Se tiver vogal adiciona + 1 ao contador de vogais

print(cont_vogal) 