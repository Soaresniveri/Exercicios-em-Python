palavras = ["Macaco", "Banana", "Lectospirose", "Peixe", "Cachorro"]
palavras_com_A = []
palavras_sem_A = []

for palavra in palavras:
    for letra in palavra:
       if "a" in palavra.lower():
          palavras_com_A.append(palavra)
       else:
          palavras_sem_A.append(palavra)

print(palavras_sem_A)