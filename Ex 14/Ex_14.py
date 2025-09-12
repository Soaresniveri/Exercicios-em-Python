numeros = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
indice = 0          

while indice < len(numeros):      # percorre enquanto houver elementos
    numero_atual = numeros[indice]
    
    if numero_atual > 50:         # verifica se o número é maior que 50
        break                     # se for, para o laço
    
    print(numero_atual)            # imprime o número atual
    indice += 1                    # passa para o próximo índice
