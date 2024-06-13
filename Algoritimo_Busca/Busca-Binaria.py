def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
alvo = 9
resultado = busca_binaria(lista, alvo)
print(f"O numero {alvo} está na posição {resultado} da lista.")