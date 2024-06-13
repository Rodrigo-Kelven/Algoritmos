def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] #key recebe o indice do array perrcorido pelo FOR
        # guarda o valor deste j, esta poha vai ser usada na linha 9!!
        j = i - 1
        #se voce estranhar isto, leia com cuidado
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] #aqui ocorre uma TROCA dos valores (recebe) o valor
            j -= 1 #aqui ele pega os indice 0,1 e os troca, e VOLTA PARA O WHILE, NAO SAI DO WHILE!!!!
        arr[j + 1] = key
    return arr

# Exemplo de uso
arr = [13, 11, 1]
print(insertion_sort(arr))