def selection_sort(arr):
    n = len(arr) #n recebe o tamanho do array
    for i in range(n): #percorre o range de N
        min_idx = i #o valor de i e armazenado 
        for j in range(i + 1, n): #percorre o range iniciando em i + 1, finalizando em N
            if arr[j] < arr[min_idx]: # se o valor de j foir menor
                min_idx = j #min_idx passa a ser J
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # aqui ocorre uma troca de posicoes
    return arr 

# Exemplo de uso
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))