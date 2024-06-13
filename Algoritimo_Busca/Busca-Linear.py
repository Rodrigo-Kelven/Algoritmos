def busca_linear(lista, alvo):
  for i in range(len(lista)):
      if lista[i] == alvo:
          return i
  return -1

arr = [2,5,4,7,8,9]
alvo = 4
resultado = busca_linear(arr, alvo)
print(f"O {alvo} está no indice: {resultado}")