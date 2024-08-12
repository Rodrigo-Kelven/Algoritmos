def counting_sort(arr):
    max_val = max(arr) # encontra o valor máximo deste array
    m = max_val + 1 # m recebe o valor máximo + 1
    count = [0] * m 

    for a in arr:
        count[a] += 1
    
    i = 0
    for a in range(m):
        for _ in range(count[a]):
            arr[i] = a
            i += 1
    return arr

# Exemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(arr))
print(f"Tamanho do array: {len(arr)}")
