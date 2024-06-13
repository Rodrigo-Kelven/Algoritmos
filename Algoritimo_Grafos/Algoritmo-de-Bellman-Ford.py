def bellman_ford(grafo, inicio):
  distancias = {vertice: float('inf') for vertice in grafo}
  distancias[inicio] = 0

  for _ in range(len(grafo) - 1):
      for vertice in grafo:
          for vizinho, peso in grafo[vertice].items():
              if distancias[vertice] + peso < distancias[vizinho]:
                  distancias[vizinho] = distancias[vertice] + peso

  for vertice in grafo:
      for vizinho, peso in grafo[vertice].items():
          if distancias[vertice] + peso < distancias[vizinho]:
              return "Ciclo de peso negativo detectado"

  return distancias

# Exemplo de uso:
grafo = {
  'A': {'B': 5, 'C': 3},
  'B': {'C': 2, 'D': 1},
  'C': {'B': 2, 'D': 4, 'E': 2},
  'D': {'E': 1},
  'E': {}
}

inicio = 'A'
print(bellman_ford(grafo, inicio))
