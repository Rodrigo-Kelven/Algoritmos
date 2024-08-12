def bubble_sort(arr):
    n = len(arr) #reserve o valor do tamanho do array em n
    for i in range(n): #percorra n de i em i
        for j in range(0, n-i-1): #percorra j, iniciando em 0 e terminando em n-1-1 = 5
            if arr[j] > arr[j+1]: #se o array j for maior que o array j+1
                arr[j], arr[j+1] = arr[j+1], arr[j] # troque os arrays de posição, ou lugar
    return arr # senao retorne o array

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
